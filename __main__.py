import xml.etree.ElementTree as ET

from smarthome import Openhab, Unit, Area, Format, Function, Channel
from xsdata.formats.dataclass.parsers import XmlParser
from FileGenerators.OpenhabItemFileGenerator import OpenhabItemFileGenerator
from FileGenerators.OpenhabKNXThingFileGenerator import OpenhabKNXThingFileGenerator
import os

def main(): 

    itemfileGenerator = OpenhabItemFileGenerator(os.path.dirname(__file__))
    thingfileGenerator = OpenhabKNXThingFileGenerator(os.path.dirname(__file__))
    parser = XmlParser()
    openhab = parser.parse("SmartHomeConfiguration.xml", Openhab)
    itemfileGenerator.writeFile(openhab.devices.device, openhab.groups.group)
    thingfileGenerator.writeBridge(openhab.knx_configuration, openhab.devices.device)



if __name__ == "__main__":
    main()

