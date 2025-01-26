from FileGenerators.OpenhabFileGenerator import OpenhabFileGenerator
from smarthome import Openhab, Unit, Area, Format, Function, Channel, Device, Comm, Groups, Group
import os
from typing import cast


EXPORTDIRECTORY = "export"
ITEMDIRECTORY = "items"
ITEMFILEKNX = "knx.items"

class OpenhabItemFileGenerator(OpenhabFileGenerator):
    def __init__(self, file_location : str) -> None:
        self.currentDeviceName = ""
        self.umlaut_map = str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"})
        self.file_location = file_location
        super().__init__()


    def writeFile(self,devices : list[Device], groups: list[Group], file_name:str):

        self.abs_file_path = os.path.join(self.file_location, EXPORTDIRECTORY+ "\\" + ITEMDIRECTORY + "\\" + file_name)
        self.file = open(self.abs_file_path, "w+",-1,"utf-8")



        self.file.write("\n")
        #Write all devices -> items
        for device in devices:
            if device.enable == True:
                for channel in device.channel:
                    if channel.enable == True:
                        self.writeRow(device,channel, groups)
                
        # Close the handle independent what happened
        self.file.close()

    def writeGroups(self, group: Group):
        self.file.write("Group ")
        self.file.write(group.name.translate(self.umlaut_map))
        if group.function:
            self.file.write(":" + group.function.value)
        self.file.write(" ")
        self.file.write("\"")
        self.file.write(group.label)
        self.file.write("\"")
        self.file.write(" ")
        self.file.write("<")
        self.file.write(group.icon.value)
        self.file.write(">")
        self.file.write(" ")
        
        if len(group.group_ref) > 0:
            self.file.write("(")
        
        groupstring = ""
        for g2 in group.group_ref:
            g3 = cast(Channel.Groups.GroupRef,g2)
            groupstring += (g3.refid)
            groupstring +=(",")
        self.file.write(groupstring.rstrip(",").translate(self.umlaut_map))

        if len(group.group_ref) > 0:
            self.file.write(")")
        
        self.file.write("\n")
        

    def writeRow(self, device : Device, channel : Channel, groups: list[Group]):
        if self.currentDeviceName != device.device_name or not self.currentDeviceName:
            self.currentDeviceName = device.device_name
            self.file.write("\n")

        self.writeType(channel)
        name = self.writeName(device,channel)
        self.writeLabel(channel)
        self.writeIcon(channel)
        self.writeGroup(channel,groups)
        self.writeTag(channel)
        if device.device_comm_type == Comm.KNX:
            if channel.type_value == channel.type_value.DATETIME_CONTROL:
                self.writeKNXDateTimeBindingConfiguration(name,device, channel) 
            elif channel.connection.knx:
                self.writeKNXBindingConfiguration(name,device, channel) 
        elif device.device_comm_type == Comm.ICAL:
            self.writeICALBindingConfiguration(name,device, channel)
        elif device.device_comm_type == Comm.NTP:
            self.writeNTPBindingConfiguration(name,device, channel)
        elif device.device_comm_type == Comm.EKEY:
            self.writeEKEYBindingConfiguration(channel.name,device, channel)
        elif device.device_comm_type == Comm.HTTP:
            self.writeDOORBindingConfiguration(name,device, channel)
        elif device.device_comm_type == Comm.ALEXA:
             self.writeAlexaBindingConfiguration(name,device, channel)
        self.file.write("\n")




    def writeType(self,channel : Channel):
        if channel.type_value == channel.type_value.DATETIME_CONTROL:
            self.file.write("DateTime" + " ")
        else:
            self.file.write(channel.type_value.value + " ")
        self.file.write(" ")

    def writeName(self, device : Device, channel : Channel):
        if channel.extention:
            name = device.device_area.value + "_" +  channel.access.value+ "_" + device.device_function.value + "_" + channel.extention + "_" +  channel.name 
        else: 
            name = device.device_area.value + "_" +  channel.access.value+ "_" + device.device_function.value + "_" + channel.name 
        name = name.replace(" ", "_")
        name = name.replace("/", "_")
        name = name.translate(self.umlaut_map)
        self.file.write(name)
        self.file.write(" ")
        channel.link = name
        return name

    def writeLabel(self, channel : Channel):

        if channel.format.name != "ND" and channel.unit.name != "ND":
            self.file.write("\"" + channel.label + " ["+ channel.format.value+" " + channel.unit.value + "]\" ")
        elif channel.format.name != "ND":
            self.file.write("\"" + channel.label + " ["+ channel.format.value + "]\" ")
        else:
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
        for group in channel.groups.group_ref:
            matches = [x for x in groups if x.id == group.refid]
            if len(matches) > 0:
                groupString += matches[0].name.translate(self.umlaut_map)
                groupString += ","
        self.file.write(groupString.rstrip(",").translate(self.umlaut_map))
        self.file.write(endDelmiter)
        self.file.write(" ")

    def writeTag(self, channel: Channel):
        #self.file.write(channel.tag)
        #self.file.write(" ")
        pass

    def writeMetaData(self, device : Device, channel : Channel):
        #seperator to seperate different 
        self.file.write(", ")
        self.file.write("smartux=\"""\" [location=\"" + device.device_area.value + "\"")
        
        if channel.meta:
            for metadata in channel.meta.meta_attribute:
                self.file.write("," + metadata.name + "=\"" + metadata.value + "\"")
        
        if channel.unit.value != "ND":
            self.file.write("," + "unit" + "=\"" + channel.unit.value + "\"")
        self.file.write("]")

    def writeKNXBindingConfiguration(self,name: str, device : Device, channel : Channel):
        startDel = "{"
        stopDel = "}"
        self.file.write(startDel)
        self.file.write("channel=\"knx:device:bridge:generic:" + name + "\"")
        self.writeMetaData(device, channel)
        self.file.write(stopDel)
        pass


    def writeKNXDateTimeBindingConfiguration(self,name: str, device : Device, channel : Channel):
        startDel = "{"
        stopDel = "}"
        self.file.write(startDel)
        self.file.write("channel=\"knx:device:bridge:generic:" + name + "\", channel=\"ntp:ntp:master:dateTime\"")
        self.writeMetaData(device, channel)
        self.file.write(stopDel)
        pass

    def writeModbusBindingConfiguration(self,device : Device, channel : Channel):
        pass

    def writeICALBindingConfiguration(self,name :str,device : Device, channel : Channel):
        startDel = "{"
        stopDel = "}"
        self.file.write(startDel)
        self.file.write("channel=\"icalendar:eventfilter:"+ name + ":result_0#begin"+ "\"")
        self.writeMetaData(device, channel)
        self.file.write(stopDel)

    def writeNTPBindingConfiguration(self,name :str,device : Device, channel : Channel):
        startDel = "{"
        stopDel = "}"
        self.file.write(startDel)
        self.file.write("channel=\"ntp:ntp:master:dateTime"+ "\"")
        self.writeMetaData(device, channel)
        self.file.write(stopDel)

    def writeEKEYBindingConfiguration(self,name :str,device : Device, channel : Channel):
        startDel = "{"
        stopDel = "}"
        self.file.write(startDel)
        self.file.write("channel=\"ekey:cvlan:master:"+ name + "\"")
        self.writeMetaData(device, channel)
        self.file.write(stopDel)

    def writeDOORBindingConfiguration(self,name :str,device : Device, channel : Channel):
        startDel = "{"
        stopDel = "}"
        self.file.write(startDel)
        self.file.write("channel=\"http:url:door:"+name+"\"")
        self.writeMetaData(device, channel)
        self.file.write(stopDel)

    def writeAlexaBindingConfiguration(self,name :str,device : Device, channel : Channel):
        startDel = "{"
        stopDel = "}"
        self.file.write(startDel)
        name = device.device_area.value + "_"  + device.device_function.value + "_" +  device.device_name
        name = name.replace(" ", "_")
        name = name.replace("/", "_")
        name.translate(self.umlaut_map)


        self.file.write("channel=\"amazonechocontrol:echo:ivo:"+ name+ ":" +channel.connection.alexa.device_channel+"\"")
        self.writeMetaData(device, channel)
        self.file.write(stopDel)


