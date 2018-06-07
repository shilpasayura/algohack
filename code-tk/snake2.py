#!/usr/bin/python

import tkinter
import time, random

WIN_W=400
WIN_H=200
WIN_color='green'
snBodycolor="lightgreen"
snHeadcolor="yellow"
snFoodcolor="red"
speed=8

#game class
class main(tkinter.Tk):
 def __init__(self, *args, **kwargs):
  tkinter.Tk.__init__(self, *args, **kwargs)
  # Trigger Of Other Functions 
  self.crt_playgarea()
  self.crt_head()
  self.crt_settings()
  self.crt_game()
  self.bind('<Any-KeyPress>',self.head_keys)

 # Creating Score Board
 def crt_game(self):
  self.scoreboard=tkinter.Label(self, text="Score : {}".format(self.score))
  self.scoreboard.pack(anchor='n')
  return
 # Updating Score Board
 def update_game(self):
  self.score=self.score+1
  self.scoreboard['text']="Score : {}".format(self.score)
  #speed=speed+1
  return
 # Game Settings
 def crt_settings(self):
  self.x=speed
  self.y=0
  self.roadmap=[(0,0)]
  self.bodylength=5
  self.sn_target=None
  self.gamevalid=1
  self.score=0
  return

 # Creating Moving Head
 def head_keys(self, event=None):
  key=event.keysym
  if key=='Left':
   self.turn_left()
  elif key=='Right':
   self.turn_right()
  elif key=='Up':
   self.turn_up()
  elif key=='Down':
   self.turn_down()
  else:
   pass
  return

 # Left Turning Function
 def turn_left(self):
  self.x=-speed
  self.y=0
  return
 # Right Turning Function
 def turn_right(self):
  self.x=speed
  self.y=0
  return

 # Turning Up/Down Function
 def turn_up(self):
  self.x=0
  self.y=-speed
  return

 def turn_down(self):
  self.x=0
  self.y=speed
  return

 # snake Head
 def crt_head(self):
  self.snake=self.board.create_rectangle(1,1,11,11,fill=snHeadcolor)
  return

 # Create Play Area 
 def crt_playgarea(self):
  self.board=tkinter.Canvas(self, width=WIN_W, height=WIN_H, background=WIN_color)
  self.board.pack(padx=10, pady=10)
  return

 # Moving Head
 def moving_head(self):
  self.board.move(self.snake,self.x,self.y)
  x1,y1,x2,y2=self.board.coords(self.snake)
  if x1<=0 or y1<=0:
   self.x=0
   self.y=0
   self.game_loss()
  elif WIN_H<=y2 or WIN_W<=x2:
   self.x=0
   self.y=0
   self.game_loss()
  return

 # Game Lost
 def game_loss(self):
  self.board.create_text(WIN_W/2,WIN_H/2,text="Game Over"\
   ,font=('arial 48 bold'),fill='white')
  self.gamevalid=0
  return

 # Snake Moving
 def re_update(self):
  self.moving_head()
  self.update_body()
  self.sn_food()
  return

 # Snake Food
 def sn_food(self):
  if self.sn_target==None:
   x1=random.randint(15,WIN_W-15)
   y1=random.randint(15,WIN_H-15)
   self.sn_target=self.board.create_oval(x1,y1,x1+10,y1+10,fill=snFoodcolor, tag="food")
  if self.sn_target:
   x1,y1,x2,y2=self.board.coords(self.sn_target)
   if len(self.board.find_overlapping(x1,y1,x2,y2))!=1:
    self.board.delete("food")
    self.sn_target=None
    self.update_game()
  return

 # Snake Body Moving Function
 def update_body(self):
  x1,y1,x2,y2=self.board.coords(self.snake)
  x2=(x2-((x2-x1)/2))
  y2=(y2-((y2-y1)/2))
  self.roadmap.append((x2,y2))
  self.board.delete('body')
  if len(self.roadmap)>=self.bodylength:
   self.roadmap=self.roadmap[-self.bodylength:]
  self.board.create_line(tuple(self.roadmap), tag="body",width=10,fill=snBodycolor)
  return

# Script Trigger
if __name__ == '__main__':
  root=main(className="Diyabara")
  while True:
   root.update()
   root.update_idletasks()
   root.re_update()
   time.sleep(0.09)
