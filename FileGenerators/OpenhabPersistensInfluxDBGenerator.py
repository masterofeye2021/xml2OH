import os
from smarthome.smart_home_definition_v2 import Openhab, Device, Channel


EXPORTDIRECTORY = "export"
THINGDIRECTORY = "persistence"
THINGFILEKNX = "influxdb.persist"

class OpenhabPersistensInfluxDBGenerator():
    def __init__(self,  file_location: str) -> None:
        self.abs_file_path = os.path.join(file_location, EXPORTDIRECTORY+ "\\" + THINGDIRECTORY + "\\" + THINGFILEKNX)

    def generate(self, openhab: Openhab):
        with open(self.abs_file_path, "w+",-1,"utf-8") as file:
            file.write("Strategies {\n")
            file.write("    everyMinute : \"0 * * * * ?\"\n")
            file.write("    everyHour : \"0 0 * * * ?\"\n")
            file.write("    everyDay : \"0 0 0 * * ?\"\n")
            file.write("    default = everyChange\n")
            file.write("}\n\n")
            file.write("Items {\n")

            for device in openhab.devices.device:
                for channel in device.channel:
                    if channel.persistence:
                        item_name = channel.link
                        file.write(f"    {item_name} : strategy = everyChange, everyHour\n")

            file.write("}\n")
