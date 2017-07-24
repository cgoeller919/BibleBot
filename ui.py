import ConfigParser
from Tkinter import *
from cfg import *
from run import *

config = ConfigParser.ConfigParser()
config.read(open("config.cfg"))

CHANNEL = config.get("CONFIG", "CHANNEL")
VERSION = config.get("CONFIG", "VERSION")
UIR = config.get("CONFIG", "UIR")

class uiLoad(): #main ui load function

    def __init__(self, master):
        self.labelLoad()
        self.buttonLoad()

    def labelLoad(self):
        label1 = Label(root, text="Channel Name")
        label2 = Label(root, text="Bible Version")

        label1.grid(row=0, column=0, sticky=E)
        label2.grid(row=1, column=0, sticky=E)

    def buttonLoad(self):
        var = StringVar(root)
        default = TSLNS[VERSION]
        entry1 = Entry(root)
        if UIR == True:
            entry1.insert(0, CHANNEL)
            versionDrop = OptionMenu(root, var, *TSLNS.values())
            var.set(default)
        else:
            entry1.insert(0, "")
            versionDrop = OptionMenu(root, var, *TSLNS)
        # run button
        turnOn = Button(root, text="Turn On", command=bibleOn)
        turnOn.grid(row=3, column=0)
        # quit button
        turnOff = Button(root, text="Turn Off", command=store)
        turnOff.grid(row=3, column=1)
        # remember settings
        stayLI = Checkbutton(root, text="Remember These Settings")
        stayLI.grid(row=2, columnspan=2)
        # place entry 1 and dropdown
        entry1.grid(row=0, column=1)
        versionDrop.grid(row=1, column=1)


#parse methods

# class store():
#     def __init__(self):
#         self.bgapiStore()
#
#
#     def cfgStore(self):
#
#         print("hello world")
#
#     def bgapiStore(self):
#         f = open("biblegateway/biblegateway_api.cfg", "r")
#         lines = f.readlines()
#         f.close()
#         f = open("biblegateway/biblegateway_api.cfg", "w")
#         f.writelines(lines[3] + VERSION)
#         f.close()


root = Tk()
root.resizable(0,0)
a = uiLoad(root)
# root.protocol("WM_DELETE_WINDOW", store())
root.mainloop()
#store()