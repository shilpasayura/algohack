from tkinter import *
root = Tk()

labelframe = LabelFrame(root, text="This is a LabelFrame")
labelframe.pack(fill="both", expand="yes")
 
left = Label(labelframe, text="Inside the LabelFrame")
left.pack()

right = Label(labelframe, text="Inside left")
right.pack()

root.mainloop()
