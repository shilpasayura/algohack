import tkinter
import os
import random
import time
#def DrawLights():
window = tkinter.Tk()
window.config(bg = "white")
window.title("Simon")
window.geometry("1000x1000")
canvas = tkinter.Canvas(window, height = 50, width = 50, bg = "white")
green=tkinter.Button(window,height=25,width=55, bg="green")
red=tkinter.Button(window,height=25,width=55, bg="red")
blue=tkinter.Button(window,height=25,width=55, bg="blue")
yellow=tkinter.Button(window,height=25,width=55, bg="yellow")
green.grid(column=0,row=0)
red.grid(column=1,row=0)
blue.grid(column=1,row=1)
yellow.grid(column=0,row=1)
window.mainloop()
#DrawLights()
yn="yes"
while yn!="n":
    window = tkinter.Tk()
    count=1
    tempc=0
    pattern=[]
    #print simon
    print("Welcome to Simon")
    print("Click the right buttons as they appear")
    new= random.randrange(4)
    pattern.append(str(new))
    new= random.randrange(4)
    pattern.append(str(new))
    while tempc<=count:
        input()
        new= random.randrange(4)
        pattern.append(str(new))
        count+=1
        tempc=-1
        while tempc<count:
            tempc+=1
            if pattern[tempc]=="0":
                #flash green
                time.sleep(.5)
                print("Green")
            elif pattern[tempc]=="1":
                #flash red
                time.sleep(.5)
                print("Red")
            elif pattern[tempc]=="2":
                #flash blue
                time.sleep(.5)
                print("blue")
            else:
                #flash yellow
                time.sleep(.5)
                print("yerrow")
        tempc=-1
        user=[]
        while tempc<count:
            new=input("Green=0, red=1,blue=2,yellow=3")
            user.append(new)
            tempc+=1
            if pattern[tempc]==user[tempc]:
                if tempc==count:
                    print("Correct")
            else:
                print("Wrong")
                yn=input("Play Again?(Y/N): ").lower()
                tempc=count+1
