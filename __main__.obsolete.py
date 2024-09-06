
import xml.etree.ElementTree as ET
from smarthome import Openhab, Unit, Area, Format, Function, Channel
from xsdata.formats.dataclass.parsers import XmlParser

import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
from ttkbootstrap.widgets import Combobox




    # do something

class SCT:
    def __init__(self, master):
        self.master = master
        self.frame = ttk.Frame(self.master)

        label = ttk.Label(self.frame, text="Area")
        label.grid(row=0,column=0)

        label = ttk.Label(self.frame, text="R/RW")
        label.grid(row=0,column=1,padx=10, pady=10)

        label = ttk.Label(self.frame, text="Function")
        label.grid(row=0,column=2)

        label = ttk.Label(self.frame, text="Erweiterung")
        label.grid(row=0,column=3)

        label = ttk.Label(self.frame, text="Label")
        label.grid(row=0,column=4)

        label = ttk.Label(self.frame, text="Channel")
        label.grid(row=0,column=5)

        label = ttk.Label(self.frame, text="Unit")
        label.grid(row=0,column=6)

        label = ttk.Label(self.frame, text="Format")
        label.grid(row=0,column=7)

        self.areaBox = ttk.Combobox(self.frame, values=[e.value for e in Area], height=1, width=10)
        self.areaBox.grid(row=1, column=0, padx=5)

        self.rwBox = ttk.Combobox(self.frame, values=["R","RW"], height=1, width=10)
        self.rwBox.grid(row=1, column=1, padx=5)

        self.function = ttk.Combobox(self.frame, values=[e.value for e in Function], height=1, width=10)
        self.function.grid(row=1, column=2, padx=5)
        self.function.current(2)

        self.extention = ttk.Text(self.frame, height=1, width=15)
        self.extention.grid(row=1, column=3, padx=5)

        self.label = ttk.Text(self.frame, height=1, width=15)
        self.label.grid(row=1, column=4, padx=5)

        self.channel = ttk.Combobox(self.frame, values=[e.value for e in Channel], height=1, width=10)
        self.channel.grid(row=1, column=5, padx=5)
        
        self.unitBox = ttk.Combobox(self.frame, values=[e.value for e in Unit], height=1, width=10, )
        self.unitBox.grid(row=1, column=6, padx=5)

        self.format = ttk.Combobox(self.frame, values=[e.value for e in Format], height=1, width=10)
        self.format.grid(row=1, column=7, padx=5)

        button = ttk.Button(self.frame, text="add", command=self.callback)
        button.grid(row=1, column=10, padx=5)

        save = ttk.Button(self.frame, text="add", command=self.callback)
        save.grid(row=3, column=0, padx=10)

        colors = self.master.style.colors

        coldata = [
            {"text": "R/RW", "stretch": False, "width": 60},
            {"text":"Area", "width": 60},
            {"text":"Function", "width": 120},
            {"text":"Erweiterung", "width": 120},
            {"text":"Label", "width": 120},
            {"text":"Channel", "width": 60},
            {"text": "Unit", "stretch": False, "width": 60},
            {"text": "Format", "stretch": False, "width": 60},
        ]

        self.dt = Tableview(
            master=self.frame,
            coldata=coldata,
            rowdata=[],
            paginated=True,
            searchable=True,
            bootstyle=PRIMARY,
            stripecolor=(colors.light, None),
        )
        
        self.dt.grid(row=2, columnspan=8,padx=10, pady=50)


        self.frame.pack()

    def callback(self):
        row = self.frame.grid_size()[1]
        self.dt.insert_row('end',[self.rwBox.get(),self.areaBox.get(), self.function.get(), self.extention.get("1.0",'end-1c'),self.label.get("1.0",'end-1c'), self.channel.get(), self.unitBox.get(),self.format.get()])
        self.dt.load_table_data()


    def readConfiguration(self):
        parser = XmlParser()
        openhab = parser.parse("SmartHomeConfiguration.xml", Openhab)
        self.readLights(openhab.lights.light)
        self.readShutter(openhab.shutter)

    def readLights(self, lights: Openhab.Lights):
        for l in lights.light:
            self.dt.insert_row('end',[l.on.read,l.on.area,l.on.function ,l.on.channel])

def main(): 

    OpenhabItem


    root = ttk.Window()
    root.geometry('1000x500+0+0')
    root.title("SmartHome Configuration Tool (SCT)")
    app = SCT(root)
    root.mainloop()

if __name__ == "__main__":
    main()

