import xml.etree.ElementTree as ET


from FileGenerators.OpenhabDoorThingFileGenerator import OpenhabDoorThingFileGenerator
from FileGenerators.OpenhabEKEYThingFileGenerator import OpenhabEKEYThingFileGenerator
from FileGenerators.OpenhabNTPThingFileGenerator import OpenhabNTPThingFileGenerator
from smarthome import Openhab
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from FileGenerators.OpenhabItemFileGenerator import OpenhabItemFileGenerator
from FileGenerators.OpenhabICALThingFileGenerator import OpenhabICALThingFileGenerator
from FileGenerators.OpenhabKNXThingFileGenerator import OpenhabKNXThingFileGenerator
import os

from smarthome.smart_home_definition_v2 import Comm, Device


def main(): 

    itemfileGenerator = OpenhabItemFileGenerator(os.path.dirname(__file__))
    knxthingfileGenerator = OpenhabKNXThingFileGenerator(os.path.dirname(__file__))
    icalthingfileGenerator = OpenhabICALThingFileGenerator(os.path.dirname(__file__))
    ntpthingfileGenerator = OpenhabNTPThingFileGenerator(os.path.dirname(__file__))
    ekeythingFileGenerator = OpenhabEKEYThingFileGenerator(os.path.dirname(__file__))
    doorthingFileGenerator = OpenhabDoorThingFileGenerator(os.path.dirname(__file__))
    parser = XmlParser()
    openhab = parser.parse("SmartHomeConfiguration.xml", Openhab)

 
    devices = filter_devices(openhab.devices.device, Comm.KNX)
    itemfileGenerator.writeFile(devices, openhab.groups.group, "knx.items")

    devices = filter_devices(openhab.devices.device, Comm.ICAL)
    itemfileGenerator.writeFile(devices, openhab.groups.group, "ical.items")

    devices = filter_devices(openhab.devices.device, Comm.NTP)
    itemfileGenerator.writeFile(devices, openhab.groups.group, "ntp.items")

    devices = filter_devices(openhab.devices.device, Comm.EKEY)
    itemfileGenerator.writeFile(devices, openhab.groups.group, "ekey.items")

    devices = filter_devices(openhab.devices.device, Comm.HTTP)
    itemfileGenerator.writeFile(devices, openhab.groups.group, "door.items")
    
    knxthingfileGenerator.writeBridge(openhab.knx_configuration, openhab.devices.device)
    icalthingfileGenerator.writeBridge(openhab.ical_configuration, openhab.devices.device)
    ntpthingfileGenerator.writeThing(openhab.ntp_configuration, openhab.devices.device)
    ekeythingFileGenerator.writeThing(openhab.ekey_configuration, openhab.devices.device)
    doorthingFileGenerator.writeThing(openhab.door_configuration, openhab.devices.device)

    #openhab.ns_map["xsi"] = "http://www.w3.org/2001/XMLSchema-instance"
    #sopenhab.attributes["xsi:noNamespaceSchemaLocation"] = "SmartHomeDefinitionV2.xsd"

    serializer = XmlSerializer()
    new_xml_content = serializer.render(openhab, ns_map={"xsi": "http://www.w3.org/2001/XMLSchema-instance"})

    new_xml_content = new_xml_content.replace(
    "<openhab", 
    '<openhab xsi:noNamespaceSchemaLocation="SmartHomeDefinitionV2.xsd"'
)
 

    # Geändertes XML zurück in die Datei schreiben
    with open("SmartHomeConfiguration.xml", "w", encoding="utf-8") as file:
        file.write(new_xml_content)

def filter_devices(device: Device,  com_type : Comm):
    data = []
    for dev in device:
        if dev.device_comm_type == com_type:
            data.append(dev)
    return data

if __name__ == "__main__":
    main()

