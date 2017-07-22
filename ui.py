from Tkinter import *
from cfg import *
from run import bibleOn

class uiLoad(): #main ui load function

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.labelLoad()
        self.buttonLoad()
        self.gridLoad()

    def labelLoad(self):
        global label1, label2
        label1 = Label(root, text="Channel Name")
        label2 = Label(root, text="Bible Version")

    def buttonLoad(self):
        global versionDrop, entry1
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
        turnOn.grid(row=3, column=1)
        # remember settings
        stayLI = Checkbutton(root, text="Remember These Settings")
        stayLI.grid(row=2, columnspan=2)

    def gridLoad(self):

        label1.grid(row=0, column=0, sticky=E)
        label2.grid(row=1, column=0, sticky=E)
        entry1.grid(row=0, column=1)
        versionDrop.grid(row=1, column=1)

#parse methods

#def store():
#    with open('config.txt', 'r') as file:
#        data = file.readlines()
#    data[1] = 'test'
#    data[2] = 'test'
#    with open('config.txt', 'r') as file:
#       file.writelines(data)

root = Tk()
root.resizable(0,0)
b = uiLoad(root)
#root.protocol("WM_DELETE_WINDOW", store())
root.mainloop()