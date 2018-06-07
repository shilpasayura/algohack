#!/usr/bin/python

PLAY_WIDTH=700
PLAY_HEIGHT=400
PLAY_CLR='green'
SN_HD_CLR="brown"
SN_SPEED=8

# Import Modules
try:
 import Tkinter
except:
 import tkinter as Tkinter
import time, random

# Main Function
class main(Tkinter):
 def __init__(*args, **kwargs):
  Tkinter.__init__( *args, **kwargs)
  # Trigger Of Other Functions 
  self.create_playground()
  self.create_snake_head()
  self.create_snake_settings()
  self.create_score_board()
  self.bind('<Any-KeyPress>',self.connecting_head_with_keys)

 # Creating Score Board
 def create_score_board(self):
  self.scoreboard=Tkinter.Label(self, text="Score : {}".format(self.score))
  self.scoreboard.pack(anchor='n')
  return
 # Updating Score Board
 def update_score_board(self):
  self.score=self.score+1
  self.scoreboard['text']="Score : {}".format(self.score)
  #SN_SPEED=SN_SPEED+1
  return
 # Creating Snake Moving Settings
 def create_snake_settings(self):
  self.x=SN_SPEED
  self.y=0
  self.roadmap=[(0,0)]
  self.bodylength=3
  self.snake_target=None
  self.gamevalid=1
  self.score=0
  return
 # Creating Snake Moving Head
 def connecting_head_with_keys(self, event=None):
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
 # Creating Turning Function
 def turn_left(self):
  self.x=-SN_SPEED
  self.y=0
  return
 # Creating Turning Function
 def turn_right(self):
  self.x=SN_SPEED
  self.y=0
  return
 # Creating Turning Function
 def turn_up(self):
  self.x=0
  self.y=-SN_SPEED
  return
 # Creating Turning Function
 def turn_down(self):
  self.x=0
  self.y=SN_SPEED
  return
 # Creating snake Head
 def create_snake_head(self):
  self.snake=self.board.create_rectangle(1,1,11,11,fill=SN_HD_CLR)
  return
 # Creating Ground
 def create_playground(self):
  self.board=Tkinter.Canvas(self, width=PLAY_WIDTH, height=PLAY_HEIGHT, background=PLAY_CLR)
  self.board.pack(padx=10, pady=10)
  return
 # Function For Moving Head
 def moving_snake_head(self):
  self.board.move(self.snake,self.x,self.y)
  x1,y1,x2,y2=self.board.coords(self.snake)
  if x1<=0 or y1<=0:
   self.x=0
   self.y=0
   self.game_loss()
  elif PLAY_HEIGHT<=y2 or PLAY_WIDTH<=x2:
   self.x=0
   self.y=0
   self.game_loss()
  return
 # Game Loss
 def game_loss(self):
  self.board.create_text(PLAY_WIDTH/2,PLAY_HEIGHT/2,text="Game Over"\
   ,font=('arial 60 bold'),fill='red')
  self.gamevalid=0
  return
 # Snake Regularly Moving
 def re_update(self):
  self.moving_snake_head()
  self.update_snake_body_structure()
  self.food_of_snake()
  return
 # Snake Food
 def food_of_snake(self):
  if self.snake_target==None:
   x1=random.randint(15,PLAY_WIDTH-15)
   y1=random.randint(15,PLAY_HEIGHT-15)
   self.snake_target=self.board.create_oval(x1,y1,x1+10,y1+10,fill='yellow', tag="food")
  if self.snake_target:
   x1,y1,x2,y2=self.board.coords(self.snake_target)
   if len(self.board.find_overlapping(x1,y1,x2,y2))!=1:
    self.board.delete("food")
    self.snake_target=None
    self.update_score_board()
  return
 # Creating Snake Body Moving Function
 def update_snake_body_structure(self):
  x1,y1,x2,y2=self.board.coords(self.snake)
  x2=(x2-((x2-x1)/2))
  y2=(y2-((y2-y1)/2))
  self.roadmap.append((x2,y2))
  self.board.delete('body')
  if len(self.roadmap)>=self.bodylength:
   self.roadmap=self.roadmap[-self.bodylength:]
  self.board.create_line(tuple(self.roadmap), tag="body",width=10,fill=SN_HD_CLR)
  return

# Script Trigger
if __name__ == '__main__':
  root=main(className=" Snake Game ")
  while True:
   root.update()
   root.update_idletasks()
   root.re_update()
   time.sleep(0.09)
