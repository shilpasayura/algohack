from tkinter import *
import tkinter

top = Tk()

mb=  Menubutton ( top, text="Food", relief=RAISED )
mb.grid()
mb.menu  =  Menu ( mb, tearoff = 0 )
mb["menu"]  =  mb.menu
    
mayoVar  = IntVar()
ketchVar = IntVar()

mb.menu.add_checkbutton ( label="Rice",
                          variable=mayoVar )
mb.menu.add_checkbutton ( label="Kottu",
                          variable=ketchVar )

mb.pack()
top.mainloop()
