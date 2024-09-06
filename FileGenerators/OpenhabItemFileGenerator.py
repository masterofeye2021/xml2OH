from FileGenerators.OpenhabFileGenerator import OpenhabFileGenerator
from smarthome import Openhab, Unit, Area, Format, Function, Channel, Device, Comm, Groups
import os



EXPORTDIRECTORY = "export"
ITEMDIRECTORY = "items"
ITEMFILEKNX = "knx.items"

class OpenhabItemFileGenerator(OpenhabFileGenerator):
    def __init__(self, file_location : str) -> None:
        
        abs_file_path = os.path.join(file_location, EXPORTDIRECTORY+ "\\" + ITEMDIRECTORY + "\\" + ITEMFILEKNX)
        self.file = open(abs_file_path, "w+")
        super().__init__()


    def writeFile(self,devices : list[Device]):
        for device in devices:
            if device.device_comm_type == Comm.KNX:
                for channel in device.channel:
                    self.writeRow(device,channel)
        # Close the handle independent what happened
        self.file.close()

    def writeRow(self, device : Device, channel : Channel):
        self.writeType(channel)
        self.writeName(device,channel)
        self.writeLabel(channel)
        self.writeIcon(channel)
        self.writeGroup(channel)
        self.writeTag(channel)
        self.writeBindingConfiguration()


    def writeType(self,channel : Channel):
        self.file.write(channel.type_value.value)
        

    def writeName(self, device : Device, channel : Channel):
        name = device.device_area.value + channel.access.value+ device.device_function.value + channel.name
        self.file.write(name)
        pass

    def writeLabel(self, channel : Channel):
        self.file.write(channel.label)
        pass

    def writeIcon(self, channel : Channel):
        startDelimiter = "<"
        endDelmiter = ">"
        self.file.write(startDelimiter + channel.icon.value + endDelmiter)
        pass

    def writeGroup(self, channel : Channel, groups : Groups):
        startDelimiter = "("
        endDelmiter = ")"

        self.file.write(startDelimiter)
        for group in channel.groups.group:
            group.refid in  groups.group
             self.file.write(group.)
        self.file.write(endDelmiter)

    def writeTag(self, channel: Channel):
        self.file.write(channel.tag)
        pass

    def writeBindingConfiguration(self):
        startDel = "{"
        stopDel = "{"
        pass

    def writeKNXBindingConfiguration(self):
        pass

    def writeModbusBindingsConfiguration(self):
        pass
