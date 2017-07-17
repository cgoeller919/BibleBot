from Tkinter import *
from cfg import *
import run

root = Tk()
var = StringVar(root)
var.set("")

#channel name
label1 = Label(root, text="Channel Name")
entry1 = Entry(root)
label1.grid(row=0, column=0, sticky=E)
entry1.grid(row=0, column=1)

#bible version
label2 = Label(root, text="Bible Version")
label2.grid(row=1, column=0, sticky=E)
versionDrop = OptionMenu(root, var, *TSLNS)
versionDrop.grid(row=1, column=1)

#run button
turnOn = Button(root, text="Turn On", command=run.BibleBot)
turnOn.grid(row=3, column=1)

#stay logged in
stayLI = Checkbutton(root, text="Remember These Settings")
stayLI.grid(row=2, columnspan=2)

#call window
root.mainloop()