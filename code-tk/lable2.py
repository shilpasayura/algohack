from tkinter import *

root = Tk()

var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )

var.set("How are you today?")
label.pack()
root.mainloop()
