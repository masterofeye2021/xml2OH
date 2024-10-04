from FileGenerators.OpenhabFileGenerator import OpenhabFileGenerator
from smarthome import Channel, Device, Comm, Group, KnxConfiguration, TypeValue
import os



EXPORTDIRECTORY = "export"
THINGDIRECTORY = "things"
THINGFILEKNX = "knx.things"

class OpenhabKNXThingFileGenerator(OpenhabFileGenerator):
    def __init__(self, file_location : str) -> None:
        self.umlaut_map = str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"})
        abs_file_path = os.path.join(file_location, EXPORTDIRECTORY+ "\\" + THINGDIRECTORY + "\\" + THINGFILEKNX)
        self.file = open(abs_file_path, "w+",-1,"utf-8")
        super().__init__()


    def writeBridge(self,knx : KnxConfiguration, devices : list[Device]):
        self.file.write("Bridge knx:ip:bridge [")
        self.file.write("\n\t")

        self.file.write("type=\"" + knx.bridge.type_value + "\",")
        self.file.write("\n\t")

        self.file.write("ipAddress=\"" + knx.bridge.ip_address+ "\",")
        self.file.write("\n\t")

        self.file.write("portNumber=" + knx.bridge.port_number+ ",")
        self.file.write("\n\t")

        self.file.write("localIp=\"" + knx.bridge.local_ip+ "\",")
        self.file.write("\n\t")

        self.file.write("readingPause=" + str(knx.bridge.reading_pause)+ ",")
        self.file.write("\n\t")

        self.file.write("responseTimeout=" +  str(knx.bridge.response_timeout)+ ",")
        self.file.write("\n\t")

        self.file.write("readRetriesLimit=" +  str(knx.bridge.read_retries_limit)+ ",")
        self.file.write("\n\t")

        self.file.write("autoTeconnectPeriod=" +  str(knx.bridge.read_retries_limit))
        self.file.write("\n")

        self.file.write("] {")
        self.file.write("\n\t")

        self.writeThing(knx,devices)


    def writeThing(self, knx : KnxConfiguration, devices : list[Device]):
        self.file.write("Thing device generic [")
        self.file.write("\n\t\t")

        self.file.write("type=\"" + knx.tunnel.address + "\",")
        self.file.write("\n\t\t")

        self.file.write("fetch=" + str(knx.tunnel.fetch).lower() + ",")
        self.file.write("\n\t\t")

        self.file.write("pingInterval=" + str(knx.tunnel.ping_interval)+ ",")
        self.file.write("\n\t\t")

        self.file.write("readInterval=" + str(knx.tunnel.read_interval))
        self.file.write("\n\t\t")

        self.file.write("] {")
        self.file.write("\n\t\t\t")

        self.writeChannel(knx, devices)

    def writeChannel(self, knx : KnxConfiguration, devices : list[Device]):

        for device in devices:
            if device.device_comm_type == Comm.KNX :
                for channel in device.channel:
                    self.writeChannelType(channel.type_value.value)
                    self.writeChannelName(device,channel)
                    self.writeChannelLabel(device,channel)
                    self.writeGroupAddress(channel)
                    self.file.write("\n\t\t\t")
        self.file.write("\n\t\t")
        self.file.write("}")
        self.file.write("}")

    def writeChannelType(self, type : str):
        self.file.write("Type " + type.lower())

    def writeChannelName(self, device : Device, channel: Channel):
        name = device.device_area.value + "_" +  channel.access.value+ "_" + device.device_function.value + "_" + channel.extention + "_" +  channel.name 
        name = name.replace(" ", "_")
        name = name.replace("/", "_")

        self.file.write("\t\t : " + name.translate(self.umlaut_map))


    def writeChannelLabel(self, device : Device, channel: Channel):
        self.file.write("\t\t \"" + channel.name + "\"")

    def writeGroupAddress(self,channel: Channel):
        if channel.type_value == TypeValue.CONTACT:
            self.file.write("\t\t [ ga=\"<"+ str(channel.connection.knx.add1.main_ga.main) + "/" + str(channel.connection.knx.add1.main_ga.middle) +"/"+ str(channel.connection.knx.add1.main_ga.sub)+"\" ]")

        if channel.type_value == TypeValue.NUMBER or channel.type_value == TypeValue.STRING:
            self.file.write("\t\t [ ga=\"<"+ str(channel.connection.knx.add1.main_ga.main) + "/" + str(channel.connection.knx.add1.main_ga.middle) +"/"+ str(channel.connection.knx.add1.main_ga.sub)+"\" ]")

        if channel.type_value == TypeValue.ROLLERSHUTTER:
            upDownMainGa = str(channel.connection.knx.add1.main_ga.main) + "/" + str(channel.connection.knx.add1.main_ga.middle) +"/"+ str(channel.connection.knx.add1.main_ga.sub)
            
            stopMainGa = str(channel.connection.knx.add2.main_ga.main) + "/" + str(channel.connection.knx.add2.main_ga.middle) +"/"+ str(channel.connection.knx.add2.main_ga.sub)
            
            positionMainGa = str(channel.connection.knx.add3.main_ga.main) + "/" + str(channel.connection.knx.add3.main_ga.middle) +"/"+ str(channel.connection.knx.add3.main_ga.sub)
            

            self.file.write("\t\t [ ")
            if channel.connection.knx.add1.main_ga.is_readable: 
                self.file.write("upDown=\"<"+ upDownMainGa +"\",")
            elif channel.connection.knx.add1.listening_ga != None:
                upDownListeningGa = str(channel.connection.knx.add1.listening_ga.main) + "/" + str(channel.connection.knx.add1.listening_ga.middle) +"/"+ str(channel.connection.knx.add1.listening_ga.sub)
                self.file.write("upDown=\"<"+ upDownMainGa + "+<"+ upDownListeningGa +"\",")
            else:
                self.file.write("upDown=\""+ upDownMainGa +"\",")

            if channel.connection.knx.add2.main_ga.is_readable: 
                self.file.write("stopMove=\"<"+ stopMainGa +"\",")
            elif channel.connection.knx.add2.listening_ga != None:
                stopListeningGa= str(channel.connection.knx.add2.listening_ga.main) + "/" + str(channel.connection.knx.add2.listening_ga.middle) +"/"+ str(channel.connection.knx.add2.listening_ga.sub)
                self.file.write("stopMove=\"<"+ stopMainGa + "+<"+ stopListeningGa +"\",")
            else:
                self.file.write("stopMove=\""+ stopMainGa +"\",")

            if channel.connection.knx.add3.main_ga.is_readable: 
                self.file.write("position=\"<"+ positionMainGa +"\"")
            elif channel.connection.knx.add3.listening_ga != None:
                positionListeningGa = str(channel.connection.knx.add3.listening_ga.main) + "/" + str(channel.connection.knx.add3.listening_ga.middle) +"/"+ str(channel.connection.knx.add3.listening_ga.sub)
                self.file.write("position=\""+ positionMainGa + "+<"+ positionListeningGa +"\"")
            else:
                self.file.write("position=\""+ positionMainGa +"\"")

            self.file.write("]")
        
        if channel.type_value == TypeValue.SWITCH:
            mainGa = str(channel.connection.knx.add1.main_ga.main) + "/" + str(channel.connection.knx.add1.main_ga.middle) +"/"+ str(channel.connection.knx.add1.main_ga.sub)
            self.file.write("\t\t [ ")
            if channel.connection.knx.add1.main_ga.is_readable: 
                self.file.write("ga=\"<"+ mainGa +"\"")
            elif channel.connection.knx.add1.listening_ga != None:
                listeningGa = str(channel.connection.knx.add1.listening_ga.main) + "/" + str(channel.connection.knx.add1.listening_ga.middle) +"/"+ str(channel.connection.knx.add1.listening_ga.sub)
                self.file.write("ga=\"<"+ mainGa + "+<"+ listeningGa +"\"")
            else:
                self.file.write("ga=\""+ mainGa +"\"")
            
            self.file.write("]")