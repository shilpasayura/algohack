#Rainbow Challenge
import turtle

myPen = turtle.Turtle()
myPen.shape("turtle")
myPen.speed(500)

window = turtle.Screen()
window.bgcolor("#69C5FF")

rainbowColors = ["#FF0000","#FFA600","#FFFF00", "#62FF00", "#1E56FC","#4800FF","#CC00FF","#69C5FF"]

size=180

myPen.penup()
myPen.goto(0,-360)

for color in rainbowColors:
  myPen.color(color)
  myPen.fillcolor(color)
  myPen.begin_fill()
  myPen.circle(size)
  myPen.end_fill()
  size -= 10
  
