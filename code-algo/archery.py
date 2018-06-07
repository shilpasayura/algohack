#Archery Challenge
import turtle
import random
import math

def drawCircle(pen, colorFill, size, x, y):
  pen.penup()
  pen.color(colorFill)
  pen.fillcolor(colorFill)
  pen.goto(x,y)
  pen.begin_fill()
  pen.circle(size)
  pen.end_fill()
  pen.pendown()
    
def drawTarget(pen):
  drawCircle(pen, "#000000", 152, 0,-152)
  drawCircle(pen, "#FFFFFF", 150, 0,-150)
  drawCircle(pen, "#000000", 120, 0,-120)
  drawCircle(pen, "#33AAFF", 90, 0,-90)
  drawCircle(pen, "#FF0000", 60, 0,-60)
  drawCircle(pen, "#FFFF00", 30, 0,-30)

def drawCross(pen, color, size, x, y):
  pen.pensize(3)
  pen.color(color)
  pen.penup()
  pen.goto(x-size,y-size)
  pen.pendown()
  pen.goto(x+size,y+size)
  pen.penup()
  pen.goto(x-size,y+size)
  pen.pendown()
  pen.goto(x+size,y-size)

def writeScore(pen, text):
  pen.penup()
  pen.goto(-80, 170)
  pen.color("#000000")
  pen.write(text, None, None, "16pt bold")

def calculateScore(arrowx,arrowy):
  score = 0
  distance = 0
  #Add code here using Pythagoras formula to calculate the distance to the centre.
  #distance = ....
  distance=round(math.sqrt(arrowx * arrowx + arrowy *arrowy))
  print(distance)
  
  #Add IF statements to decide the final score to return
  #distance between 0 - 30 (Yellow) = 10 points
  #distance between 31 - 60 (Red) = 5 points
  #distance between 61 - 90 (Blue) = 3 points
  #distance between 91 - 120 (Black) = 2 points
  #distance between 121 - 150 (White) = 1 point
  #distance above 150 - off target = 0 point

  if ((distance >=0) and (distance < 31)):
    score=10
  elif ((distance >=30) and (distance < 61)):
    score=5
  elif ((distance >=61) and (distance < 91)):
    score=3
  elif ((distance >=91) and (distance < 121)):
    score=2
  else:
    score=0
  return(score)
  
#Main Program Starts Here
myPen = turtle.Turtle()
#myPen.tracer(0)
myPen.speed(0)
myPen.shape("arrow")

drawTarget(myPen)

#Shooting the arrow
arrowx= random.randint(-150,150)
arrowy= random.randint(-150,150)
drawCross(myPen,"#FF7777",10,arrowx,arrowy)

#Calculate and display score
score = calculateScore(arrowx,arrowy)
print(score)
#writeScore(myPen,"Your Score: + " + str(score))

#Hide the pen
myPen.penup()
myPen.goto(-300,-300)

myPen.getscreen().update()	
