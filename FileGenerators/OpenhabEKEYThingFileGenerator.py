from FileGenerators.OpenhabFileGenerator import OpenhabFileGenerator
from smarthome import Device, Comm, EkeyConfiguration
import os



EXPORTDIRECTORY = "export"
THINGDIRECTORY = "things"
THINGFILEKNX = "ekey.things"


class OpenhabEKEYThingFileGenerator(OpenhabFileGenerator):
    def __init__(self, file_location : str) -> None:
        self.umlaut_map = str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"})
        abs_file_path = os.path.join(file_location, EXPORTDIRECTORY+ "\\" + THINGDIRECTORY + "\\" + THINGFILEKNX)
        self.file = open(abs_file_path, "w+",-1,"utf-8")
        super().__init__()


    def writeThing(self,ekey : EkeyConfiguration, devices : list[Device]):
        self.file.write("ekey:cvlan:master [")
        self.file.write("\n\t")

        self.file.write("ipAddress=\"" + ekey.thing.ip_address+ "\",")
        self.file.write("\n\t")

        self.file.write("port=\"" + str(ekey.thing.port)+ "\",")
        self.file.write("\n\t")

        self.file.write("protocol=\"" + ekey.thing.protocol.value + "\",")
        self.file.write("\n\t")

        self.file.write("delimiter=\"" + ekey.thing.delimiter + "\"")
        self.file.write("\n\t")

        if ekey.thing.nat_ip:
            self.file.write( "\",")
            self.file.write("serverPort=\"" +ekey.thing.nat_ip+ "\"")
            self.file.write("\n\t")

        self.file.write("]")
        


