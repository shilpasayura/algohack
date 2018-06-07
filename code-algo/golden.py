#Golden Angle
# in geometry, the golden angle is the smaller of the two angles
# created by sectioning the circumference of a circle
# according to the golden ratio.
# Golden Angle ≈ 137.5° 
# Plants have their leaves spread all around the stem to soak
# up as much sun as possible.
# Using the golden angle between two consecutive leaves
# is the most effective approach to spread the leaves around the stem.

Let’s see how this work:
import turtle
import time

def drawCircle(x, y, radius, color):
    global myPen
    myPen.setheading(0)
    myPen.penup()
    myPen.color(color)
    myPen.fillcolor(color)
    myPen.goto(x,y-radius)
    myPen.begin_fill()
    myPen.circle(radius)
    myPen.end_fill()
    myPen.pendown()
    
myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(0)

#Draw Trunc
drawCircle(0, 0, 20 , "#705623")

myPen.goto(0,0)
myPen.width(4)
goldenAngle=137.5
myPen.setheading(90)

for branch in range(0,50):
  #Draw Branch
  myPen.forward(150)
  myPen.forward(-150)
  myPen.right(goldenAngle)
  time.sleep(1)
