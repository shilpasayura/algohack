import tkinter

top = tkinter.Tk()

canvas= tkinter.Canvas(top, bg="green", height=250, width=300)

coord = 10, 50, 240, 210
arc = canvas.create_arc(coord, start=0, extent=90, fill="yellow")

canvas.pack()
top.mainloop()
