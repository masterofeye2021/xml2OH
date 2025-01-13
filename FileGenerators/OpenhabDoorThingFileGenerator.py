from FileGenerators.OpenhabFileGenerator import OpenhabFileGenerator
from smarthome import Device, Comm, DoorConfiguration, Channel
import os



EXPORTDIRECTORY = "export"
THINGDIRECTORY = "things"
THINGFILEKNX = "door.things"

# At the moment this class is just working for the MüllKalendar, means is just parses the configuration for that specific calendar

class OpenhabDoorThingFileGenerator(OpenhabFileGenerator):
    def __init__(self, file_location : str) -> None:
        self.umlaut_map = str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"})
        abs_file_path = os.path.join(file_location, EXPORTDIRECTORY+ "\\" + THINGDIRECTORY + "\\" + THINGFILEKNX)
        self.file = open(abs_file_path, "w+",-1,"utf-8")
        super().__init__()


    def writeThing(self,door : DoorConfiguration, devices : list[Device]):
        self.file.write("http:url:door [")
        self.file.write("\n\t")

        self.file.write("baseURL=\"" + door.thing.base_url + "\",")
        self.file.write("\n\t")

        self.file.write("timeout=\"" + str(door.thing.timeout)+ "\",")
        self.file.write("\n\t")

        self.file.write("refresh=\"" + str(door.thing.refresh)+ "\",")
        self.file.write("\n\t")

        self.file.write("delay=\"" + str(door.thing.delay)+ "\",")
        self.file.write("\n\t")

        self.file.write("stateMethod=\"" + door.thing.state_method.value + "\",")
        self.file.write("\n\t")

        self.file.write("stateMethod=\"" + door.thing.state_method.value + "\",")
        self.file.write("\n\t")

        self.file.write("ignoreSSLErrors=\"" + str(door.thing.ignore_sslerrors).lower() + "\",")
        self.file.write("\n\t")

        self.file.write("strictErrorHandling=\"" + str(door.thing.strict_error_handling).lower() + "\"")
        self.file.write("\n\t")
        
        if door.thing.buffer_size:
            self.file.write( ",")
            self.file.write("bufferSize=\"" + str(door.thing.buffer_size) + "\"")
            self.file.write("\n\t")


        if door.thing.username:
            self.file.write( ",")
            self.file.write("username=\"" + door.thing.username + "\"")
            self.file.write("\n\t")

        if door.thing.password:
            self.file.write( ",")
            self.file.write("password=\"" + door.thing.password + "\"")
            self.file.write("\n\t")
        
        self.file.write("] {")
        self.file.write("\n\t\t")

        self.writeChannel(door,devices)

    def writeChannel(self,door : DoorConfiguration, devices : list[Device]):
        self.file.write("Channels:")
        self.file.write("\n\t\t\t")

        for device in devices:
            if device.device_comm_type == Comm.HTTP :
                for channel in device.channel:
                    self.writeChannelType(channel.type_value.value)
                    self.writeChannelName(device,channel)
                    self.writeChannelLabel(device,channel)
                    self.writeMeta(channel)
                    self.file.write("\n\t\t\t")
        self.file.write("\n\t")
        self.file.write("}")

    def writeChannelType(self, type : str):
        self.file.write("Type " + type.lower())

    def writeChannelName(self, device : Device, channel: Channel):
        if channel.extention:
            name = device.device_area.value + "_" +  channel.access.value+ "_" + device.device_function.value + "_" + channel.extention + "_" +  channel.name 
        else: 
            name = device.device_area.value + "_" +  channel.access.value+ "_" + device.device_function.value + "_" +  channel.name 
        name = name.replace(" ", "_")
        name = name.replace("/", "_")

        self.file.write("\t\t : " + name.translate(self.umlaut_map))


    def writeChannelLabel(self, device : Device, channel: Channel):
        self.file.write("\t\t \"" + channel.name + "\"")

    def writeMeta(self,channel: Channel):
        self.file.write(" [ stateTransformation=\"JS:check_klingel.js\"")
        self.file.write(", openValue=\"OPEN\"")
        self.file.write(", closedValue=\"CLOSED\"]")