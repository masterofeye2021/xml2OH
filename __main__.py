import xml.etree.ElementTree as ET
import os
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from smarthome import Openhab
from smarthome.smart_home_definition_v2 import Comm, Device
from FileGenerators.OpenhabDoorThingFileGenerator import OpenhabDoorThingFileGenerator
from FileGenerators.OpenhabEKEYThingFileGenerator import OpenhabEKEYThingFileGenerator
from FileGenerators.OpenhabNTPThingFileGenerator import OpenhabNTPThingFileGenerator
from FileGenerators.OpenhabItemFileGenerator import OpenhabItemFileGenerator
from FileGenerators.OpenhabICALThingFileGenerator import OpenhabICALThingFileGenerator
from FileGenerators.OpenhabKNXThingFileGenerator import OpenhabKNXThingFileGenerator
from FileGenerators.OpenhabPersistensInfluxDBGenerator import OpenhabPersistensInfluxDBGenerator

# Initialize file generators with the current directory path
def initialize_generators(base_path):
    return {
        "item": OpenhabItemFileGenerator(base_path),
        "knx": OpenhabKNXThingFileGenerator(base_path),
        "ical": OpenhabICALThingFileGenerator(base_path),
        "ntp": OpenhabNTPThingFileGenerator(base_path),
        "ekey": OpenhabEKEYThingFileGenerator(base_path),
        "door": OpenhabDoorThingFileGenerator(base_path)
    }

# Parse the SmartHome configuration XML file
def parse_configuration(file_path):
    parser = XmlParser()
    return parser.parse(file_path, Openhab)

# Filter devices based on communication type
def filter_devices(devices, com_type):
    return [dev for dev in devices if dev.device_comm_type == com_type]

# Write item files for each communication type
def write_item_files(generators, openhab):
    comm_types = ["KNX", "ICAL", "NTP", "EKEY", "HTTP"]
    for comm in comm_types:
        devices = filter_devices(openhab.devices.device, getattr(Comm, comm))
        generators["item"].writeFile(devices, openhab.groups.group, f"{comm.lower()}.items")

# Write thing files for each configuration type
def write_thing_files(generators, openhab):
    generators["knx"].writeBridge(openhab.knx_configuration, openhab.devices.device)
    generators["ical"].writeBridge(openhab.ical_configuration, openhab.devices.device)
    generators["ntp"].writeThing(openhab.ntp_configuration, openhab.devices.device)
    generators["ekey"].writeThing(openhab.ekey_configuration, openhab.devices.device)
    generators["door"].writeThing(openhab.door_configuration, openhab.devices.device)

# Serialize and save the modified XML content
def save_modified_xml(openhab, file_path):
    serializer = XmlSerializer()
    new_xml_content = serializer.render(openhab, ns_map={"xsi": "http://www.w3.org/2001/XMLSchema-instance"})
    new_xml_content = new_xml_content.replace(
        "<openhab", 
        '<openhab xsi:noNamespaceSchemaLocation="SmartHomeDefinitionV2.xsd"'
    )
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(new_xml_content)

# Main function to generate OpenHAB configuration files
def main(): 
    base_path = os.path.dirname(__file__)
    generators = initialize_generators(base_path)
    openhab = parse_configuration("SmartHomeConfiguration.xml")
    
    write_item_files(generators, openhab)
    write_thing_files(generators, openhab)

    save_modified_xml(openhab, "SmartHomeConfiguration.xml")

    # Generate the persistence file
    influxdb = OpenhabPersistensInfluxDBGenerator(base_path)
    influxdb.generate(openhab)


if __name__ == "__main__":
    main()

