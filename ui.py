from Tkinter import *
from cfg import *
from run import BibleBot

root = Tk()

#channel name
label1 = Label(root, text="Channel Name")
entry1 = Entry(root)
label1.grid(row=0, column=0, sticky=E)
entry1.grid(row=0, column=1)

#bible version


#run button
run = Button(root, text="Turn On", command=BibleBot)
run.pack()

#stay logged in
stayLI = Checkbutton(root, text="Remember These Settings")
stayLI.grid(columnspan=2)

#call window
root.mainloop()