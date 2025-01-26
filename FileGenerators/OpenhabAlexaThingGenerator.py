from FileGenerators.OpenhabFileGenerator import OpenhabFileGenerator
from smarthome import Channel, Device, Comm, Group, AlexaConfiguration, Alexa, TypeValue
import os



EXPORTDIRECTORY = "export"
THINGDIRECTORY = "things"
THINGFILEKNX = "alexa.things"

# At the moment this class is just working for the MüllKalendar, means is just parses the configuration for that specific calendar

class OpenhabAlexaThingGenerator(OpenhabFileGenerator):
    def __init__(self, file_location : str) -> None:
        self.umlaut_map = str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"})
        abs_file_path = os.path.join(file_location, EXPORTDIRECTORY+ "\\" + THINGDIRECTORY + "\\" + THINGFILEKNX)
        self.file = open(abs_file_path, "w+",-1,"utf-8")
        super().__init__()


    def writeBridge(self,ax : AlexaConfiguration, devices : list[Device]):
        self.file.write("Bridge amazonechocontrol:account:ivo  \"Amazon Account\" @ \"Accounts\" [")
        self.file.write("\n\t")

        self.file.write("discoverSmartHome=" + str(ax.bridge.discover_smart_home) + ",")
        self.file.write("\n\t")

        self.file.write("pollingIntervalSmartHomeAlexa=" + str(ax.bridge.polling_interval_smart_home_alexa)+ ",")
        self.file.write("\n\t")

        self.file.write("pollingIntervalSmartSkills=" + str(ax.bridge.polling_interval_smart_skills))
        self.file.write("\n\t")

        self.file.write("] {")
        self.file.write("\n\t\t")

        self.writeThing(ax,devices)


    def writeThing(self, alexa : AlexaConfiguration, devices : list[Device]):


        for device in devices:
            if device.device_comm_type == Comm.ALEXA :
                name = device.device_area.value + "_"  + device.device_function.value + "_" +  device.device_name
                    
                name = name.replace(" ", "_")
                name = name.replace("/", "_")

                device.device_id
                for thing in alexa.thing:
                    if thing.deviceid == device.device_id:
                        self.file.write("Thing " +thing.type_value.value+ " "+ name.translate(self.umlaut_map)+ " [serialNumber=\""+ thing.serial +"\" ]")
                self.file.write("\n\t\t")
        self.file.write("}")


