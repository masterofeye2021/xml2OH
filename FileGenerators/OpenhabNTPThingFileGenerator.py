from FileGenerators.OpenhabFileGenerator import OpenhabFileGenerator
from smarthome import Device, Comm, NtpConfiguration
import os



EXPORTDIRECTORY = "export"
THINGDIRECTORY = "things"
THINGFILEKNX = "ntp.things"

# At the moment this class is just working for the MüllKalendar, means is just parses the configuration for that specific calendar

class OpenhabNTPThingFileGenerator(OpenhabFileGenerator):
    def __init__(self, file_location : str) -> None:
        self.umlaut_map = str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"})
        abs_file_path = os.path.join(file_location, EXPORTDIRECTORY+ "\\" + THINGDIRECTORY + "\\" + THINGFILEKNX)
        self.file = open(abs_file_path, "w+",-1,"utf-8")
        super().__init__()


    def writeThing(self,ntp : NtpConfiguration, devices : list[Device]):
        self.file.write("ntp:ntp:master [")
        self.file.write("\n\t")

        self.file.write("hostname=\"" + ntp.thing.hostname+ "\",")
        self.file.write("\n\t")

        self.file.write("refreshInterval=\"" + str(ntp.thing.refresh_interval)+ "\",")
        self.file.write("\n\t")

        self.file.write("refreshNtp=\"" +str(ntp.thing.refresh_ntp)+ "\"")
        self.file.write("\n\t")

        if ntp.thing.server_port:
            self.file.write( "\",")
            self.file.write("serverPort=\"" +str(ntp.thing.server_port)+ "\"")
            self.file.write("\n\t")

        if ntp.thing.time_zone:
            self.file.write( "\",")
            self.file.write("timeZone=" + ntp.thing.time_zone+ "\"")
            self.file.write("\n\t")

        self.file.write("]")
        


