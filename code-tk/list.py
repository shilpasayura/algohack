from tkinter import *
import tkinter

top = Tk()

Lb1 = Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(2, "C")
Lb1.insert(3, "PHP")
Lb1.insert(4, "Java")

Lb1.pack()
top.mainloop()
