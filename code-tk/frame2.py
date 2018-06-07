from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack( side = LEFT)


bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

greenbutton = Button(bottomframe, text="Brown", fg="brown")
greenbutton.pack( side = RIGHT )

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)

root.mainloop()
