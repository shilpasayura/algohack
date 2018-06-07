from tkinter import *
import tkinter


top = tkinter.Tk()
def hello():
   tkMessageBox.showinfo("Say Hello", "Hello GUI")

B1 = tkinter.Button(top, text = "Say Hello", command = hello)
B1.pack()

top.mainloop()
