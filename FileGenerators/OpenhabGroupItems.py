from FileGenerators.OpenhabFileGenerator import OpenhabFileGenerator
from smarthome import Openhab, Unit, Area, Format, Function, Channel, Device, Comm, Groups, Group
import os
from typing import cast


EXPORTDIRECTORY = "export"
ITEMDIRECTORY = "items"
ITEMFILEKNX = "group.items"

class OpenhabGroupItems(OpenhabFileGenerator):
    def __init__(self, file_location : str) -> None:
        self.umlaut_map = str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"})
        abs_file_path = os.path.join(file_location, EXPORTDIRECTORY+ "\\" + ITEMDIRECTORY + "\\" + ITEMFILEKNX)
        self.file = open(abs_file_path, "w+",-1,"utf-8")
        super().__init__()

    def write_group(self,openhab: Openhab):
        for group in openhab.groups.group:
            self.file.write("Group " + group.name.translate(self.umlaut_map))
            if len(group.group_ref) > 0:
                self.file.write("(")
            grouptext = ""
            for groupref in group.group_ref:
                grouptext += groupref.refid.translate(self.umlaut_map) + ","
            grouptext = grouptext.removesuffix(",")    
            self.file.write(grouptext)
            if len(group.group_ref) > 0:
                self.file.write(")")
            self.file.write("\n")

        
