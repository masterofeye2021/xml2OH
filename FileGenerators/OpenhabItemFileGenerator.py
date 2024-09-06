from FileGenerators.OpenhabFileGenerator import OpenhabFileGenerator
from smarthome import Openhab, Unit, Area, Format, Function, Channel, Device, Comm, Groups, Group
import os



EXPORTDIRECTORY = "export"
ITEMDIRECTORY = "items"
ITEMFILEKNX = "knx.items"

class OpenhabItemFileGenerator(OpenhabFileGenerator):
    def __init__(self, file_location : str) -> None:
        
        abs_file_path = os.path.join(file_location, EXPORTDIRECTORY+ "\\" + ITEMDIRECTORY + "\\" + ITEMFILEKNX)
        self.file = open(abs_file_path, "w+")
        super().__init__()


    def writeFile(self,devices : list[Device], groups: list[Group]):
        for device in devices:
            if device.device_comm_type == Comm.KNX:
                for channel in device.channel:
                    self.writeRow(device,channel, groups)
        # Close the handle independent what happened
        self.file.close()

    def writeRow(self, device : Device, channel : Channel, groups: list[Group]):
        self.writeType(channel)
        name = self.writeName(device,channel)
        self.writeLabel(channel)
        self.writeIcon(channel)
        self.writeGroup(channel,groups)
        self.writeTag(channel)
        self.writeBindingConfiguration(name)
        self.file.write("\n")


    def writeType(self,channel : Channel):
        self.file.write(channel.type_value.value + " ")
        self.file.write(" ")

    def writeName(self, device : Device, channel : Channel):
        name = device.device_area.value + "_" +  channel.access.value+ "_" + device.device_function.value + "_" + channel.extention + "_" +  channel.name 
        name = name.replace(" ", "_")
        name = name.replace("/", "_")
        self.file.write(name)
        self.file.write(" ")
        return name

    def writeLabel(self, channel : Channel):
        self.file.write("\"" + channel.label + "\"")
        self.file.write(" ")
        pass

    def writeIcon(self, channel : Channel):
        startDelimiter = "<"
        endDelmiter = ">"
        self.file.write(startDelimiter + channel.icon.value + endDelmiter)
        self.file.write(" ")
        pass

    def writeGroup(self, channel : Channel, groups : list[Group]):
        startDelimiter = "("
        endDelmiter = ")"
        
        self.file.write(startDelimiter)
        groupString = ""
        for group in channel.groups.group:
            matches = [x for x in groups if x.id == group.refid]
            if len(matches) > 0:
                groupString += matches[0].name
                groupString += ","
        self.file.write(groupString.rstrip(","))
        self.file.write(endDelmiter)
        self.file.write(" ")

    def writeTag(self, channel: Channel):
        #self.file.write(channel.tag)
        #self.file.write(" ")
        pass

    def writeBindingConfiguration(self, name: str):
        startDel = "{"
        stopDel = "}"
        self.file.write(startDel)
        self.file.write("channel=\"knx:device:bridge:generic:" + name + "\"")
        self.file.write(stopDel)
        pass

    def writeKNXBindingConfiguration(self):
        pass

    def writeModbusBindingsConfiguration(self):
        pass
