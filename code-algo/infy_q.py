#Infinite Quarter Series
#The infinite quarter series is a series where each term is a quarter of the previous one:
# 1/4 > 1/16 > 1/64 > 1/256
#We can visually represent this by dividing a canvas into 4 quadrants and colouring in one quadrant .
#Then we repeat this process by dividing the top right quadrant into 4 and so on.

import turtle
import random

boardWidth = 40
needleLength = 30
numberOfNeedles = 50
    
myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(0)
myPen.color("#f442d1")

myPen.penup()
x=-200
y=-200
width=400
sum=0

for n in range(1,11):
  sum += (1/4)**n
  width=width/2
  #Draw + lines
  myPen.penup()
  myPen.goto(x+width,y)
  myPen.pendown()
  myPen.goto(200,y)
  myPen.penup()
  myPen.goto(x+width,y)
  myPen.pendown()
  myPen.goto(x+width,200)
  myPen.penup()
  myPen.goto(x,y)
  
  #Fill in 1/4
  myPen.begin_fill()
  myPen.goto(x+width,y)
  myPen.goto(x+width,y+width)
  myPen.goto(x,y+width)
  myPen.goto(x,y)
  myPen.end_fill()
  
  x+=width
  y+=width
  
print("After " + str(n) + " iterations:")
