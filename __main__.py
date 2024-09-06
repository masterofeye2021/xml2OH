import xml.etree.ElementTree as ET
from smarthome import Openhab, Unit, Area, Format, Function, Channel
from xsdata.formats.dataclass.parsers import XmlParser
from FileGenerators.OpenhabItemFileGenerator import OpenhabItemFileGenerator
import os

def main(): 

    fileGenerator = OpenhabItemFileGenerator(os.path.dirname(__file__))
    parser = XmlParser()
    openhab = parser.parse("SmartHomeConfiguration.xml", Openhab)
    fileGenerator.writeFile(openhab.devices.device, openhab.groups.group)
    

if __name__ == "__main__":
    main()

