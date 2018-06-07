from tkinter import *
import tkinter

def onclick():
   pass

root = Tk()
text = Text(root)
text.insert(INSERT, "Hello!")
text.insert(END, "Bye!")
text.pack()

text.tag_add("first", "1.0", "1.6")
text.tag_add("second", "1.7", "1.13")
text.tag_config("first", background="yellow", foreground="blue")
text.tag_config("second", background="red", foreground="yellow")
root.mainloop()
