from FileGenerators.OpenhabFileGenerator import OpenhabFileGenerator
from smarthome import Channel, Device, Comm, Group, IcalConfiguration, TypeValue
import os



EXPORTDIRECTORY = "export"
THINGDIRECTORY = "things"
THINGFILEKNX = "ical.things"

# At the moment this class is just working for the MüllKalendar, means is just parses the configuration for that specific calendar

class OpenhabICALThingFileGenerator(OpenhabFileGenerator):
    def __init__(self, file_location : str) -> None:
        self.umlaut_map = str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"})
        abs_file_path = os.path.join(file_location, EXPORTDIRECTORY+ "\\" + THINGDIRECTORY + "\\" + THINGFILEKNX)
        self.file = open(abs_file_path, "w+",-1,"utf-8")
        super().__init__()


    def writeBridge(self,ical : IcalConfiguration, devices : list[Device]):
        self.file.write("Bridge icalendar:calendar:bridge [")
        self.file.write("\n\t")

        self.file.write("url=\"" + ical.bridge.url + "\",")
        self.file.write("\n\t")

        self.file.write("refreshTime=\"" + ical.bridge.refresh_time+ "\",")
        self.file.write("\n\t")

        self.file.write("username=\"" + ical.bridge.username+ "\",")
        self.file.write("\n\t")

        self.file.write("password=\"" + ical.bridge.password+ "\",")
        self.file.write("\n\t")

        self.file.write("maxSize=" + str(ical.bridge.max_size))
        self.file.write("\n\t")

        self.file.write("] {")
        self.file.write("\n\t")

        self.writeThing(ical,devices)


    def writeThing(self, ical : IcalConfiguration, devices : list[Device]):


        for device in devices:
            if device.device_comm_type == Comm.ICAL :
                for channel in device.channel:
                    name =""
                    if channel.extention:
                        name = device.device_area.value + "_" +  channel.access.value+ "_" + device.device_function.value + "_" + channel.extention + "_" +  channel.name 
                    else: 
                        name = device.device_area.value + "_" +  channel.access.value+ "_" + device.device_function.value + "_" +  channel.name 
                    
                    name = name.replace(" ", "_")
                    name = name.replace("/", "_")


                    self.file.write("Thing icalendar:eventfilter:"+ name.translate(self.umlaut_map)+ " ")
                    self.file.write("\"" + channel.name + "\" ")
                    self.file.write("(" + "icalendar:calendar:bridge" + ") ")
                    self.file.write("[ maxEvents="+ str(channel.connection.ical.max_events))
                    self.file.write(", refreshTime="+ str(channel.connection.ical.refresh_time))
                    self.file.write(", datetimeUnit=\""+ str(channel.connection.ical.datetime_unit.name) +"\"")
                    self.file.write(", datetimeStart=\""+ channel.connection.ical.datetime_start +"\"")
                    self.file.write(", datetimeEnd=\""+ channel.connection.ical.datetime_end +"\"")
                    self.file.write(", textEventField=\""+ channel.connection.ical.text_event_field +"\"")
                    self.file.write(", textEventValue=\""+ channel.connection.ical.text_event_value +"\"")
                    self.file.write(", textValueType=\""+ str(channel.connection.ical.text_value_type.name) +"\"]" )
                    self.file.write("\n\t")
        self.file.write("}")


