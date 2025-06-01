from FileGenerators.OpenhabFileGenerator import OpenhabFileGenerator
from smarthome import Channel, Device, Comm, HuaweiConfiguration
import os



EXPORTDIRECTORY = "export"
THINGDIRECTORY = "things"
THINGFILEKNX = "huawei_pv.things"

# At the moment this class is just working for the MüllKalendar, means is just parses the configuration for that specific calendar

class OpenhabHuaweiPVThingGenerator(OpenhabFileGenerator):
    def __init__(self, file_location : str) -> None:
        self.umlaut_map = str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"})
        abs_file_path = os.path.join(file_location, EXPORTDIRECTORY+ "\\" + THINGDIRECTORY + "\\" + THINGFILEKNX)
        self.file = open(abs_file_path, "w+",-1,"utf-8")
        super().__init__()


    def writeBridge(self,hw : HuaweiConfiguration, devices : list[Device]):
        self.file.write("Bridge modbus:tcp:huaweipv [")
        self.file.write("\n\t")

        self.file.write("host=\"" + str(hw.bridge.ip) + "\",")
        self.file.write("\n\t")

        self.file.write("port=" + str(hw.bridge.port)+ ",")
        self.file.write("\n\t")

        self.file.write("id=" + str(hw.bridge.id)+ ",")
        self.file.write("\n\t")

        self.file.write("rtuEncoded=" + str(hw.bridge.rtu_encoding).lower()+ ",")
        self.file.write("\n\t")

        self.file.write("timeBetweenTransactionsMillis=" + str(hw.bridge.time_between_transactions)+ ",")
        self.file.write("\n\t")

        self.file.write("connectMaxTries=" + str(hw.bridge.max_reconnect))
        self.file.write("\n\t")

        self.file.write("] {")
        self.file.write("\n\t\t")

        self.writeBridgePoller(hw,devices)

        self.file.write("\n\t")
        self.file.write("}")
        self.file.write("\n\t")

    def writeBridgePoller(self, hw : HuaweiConfiguration, devices : list[Device]):

        for device in devices:
            if device.device_comm_type == Comm.MODBUS:
                # Group channels by poller address
                channels_by_address = {}
                for channel in sorted(device.channel, key=lambda ch: ch.connection.modbus.poller.address):
                    address = channel.connection.modbus.poller.address
                    if address not in channels_by_address:
                        channels_by_address[address] = []
                    channels_by_address[address].append(channel)

                
                # Iterate over grouped channels
                for address in channels_by_address.keys():
                    length = 0
                    for channel in channels_by_address[address]:
                        length += channel.connection.modbus.poller.length
    
                    self.file.write("Bridge poller " + str(address) + " \"Poller " + channel.connection.modbus.poller.name +  "\" [")
                    self.file.write("\n\t\t\t")
                    self.file.write("start=" + str(address) + ",")
                    self.file.write("\n\t\t\t")
                    self.file.write("length=" + str(length) + ",")
                    self.file.write("\n\t\t\t")
                    self.file.write("type=\"" + str(channel.connection.modbus.poller.type_value.value).lower() + "\",")
                    self.file.write("\n\t\t\t")
                    self.file.write("refresh=" + str(channel.connection.modbus.poller.refresh) + ",")
                    self.file.write("\n\t\t\t")
                    self.file.write("maxTries=" + str(channel.connection.modbus.poller.max_tries) + ",")
                    self.file.write("\n\t\t\t")
                    self.file.write("cacheMillis=" + str(channel.connection.modbus.poller.cache_millis))
                    self.file.write("]")
                    self.file.write("\n\t\t")
                    self.file.write("{")
                    

                    # Write each channel in the group
                    for channel in channels_by_address[address]:
                        self.writeThing(hw, device, channel)
                    self.file.write("\n\n\t\t")
                    self.file.write("}")
                    self.file.write("\n\n\t\t")

    def writeThing(self,  hw : HuaweiConfiguration, device : Device, channel : Channel):
                self.file.write("\n\t\t\t")
                name = device.device_area.value + "_"  + channel.name  
                name = name.replace(" ", "_")
                name = name.replace("/", "_")

                self.file.write("Thing data " + name .translate(self.umlaut_map)+ " \"Data " + channel.connection.modbus.poller.name + "\" [ ")
                
                buffer = ""
                if channel.connection.modbus.poller.thing.read_value_type != None:
                    buffer += "readValueType=\"" + str(channel.connection.modbus.poller.thing.read_value_type.value) + "\","

                if channel.connection.modbus.poller.thing.read_start != None:
                    buffer += "readStart=" + str(channel.connection.modbus.poller.thing.read_start) + ","
                
                if channel.connection.modbus.poller.thing.read_transform != None:
                    buffer += "readTransform=" + str(channel.connection.modbus.poller.thing.read_transform) + ","
                
                if channel.connection.modbus.poller.thing.write_value_type != None:
                    buffer += "writeValueType=" + str(channel.connection.modbus.poller.thing.write_value_type) + ","

                if channel.connection.modbus.poller.thing.write_start != None:
                    buffer += "writeStart=" + str(channel.connection.modbus.poller.thing.write_start) + ","

                if channel.connection.modbus.poller.thing.write_type != None:
                    buffer += "writeType=" + str(channel.connection.modbus.poller.thing.write_type) + ","

                if channel.connection.modbus.poller.thing.write_transform != None:
                    buffer += "writeTransform=" + str(channel.connection.modbus.poller.thing.write_transform) + ","

                if channel.connection.modbus.poller.thing.write_multiple_even_with_single_register_or_coil != None:
                    buffer += "writeMultipleEvenWithSingleRegisterOrCoil=" + str(channel.connection.modbus.poller.thing.write_multiple_even_with_single_register_or_coil).lower() + ","
                
                if channel.connection.modbus.poller.thing.write_max_tries != None:
                    buffer += "writeMaxTries=" + str(channel.connection.modbus.poller.thing.write_max_tries) + ","

                if channel.connection.modbus.poller.thing.update_unchanged_values_every_millis != None:
                    buffer += "updateUnchangedValuesEveryMillis=" + str(channel.connection.modbus.poller.thing.update_unchanged_values_every_millis) + ","

                buffer = buffer.removesuffix(",")
                self.file.write(buffer)
                self.file.write("]")




