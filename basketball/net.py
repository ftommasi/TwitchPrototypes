import pygame
import entity.py

class Net(Entity):
  def __init__(self,x,y,color,width=20,height=20):
    #TODO MAGIC NUMBER
    Entity.__init__(self,x,y,color,0)
    self.width = width
    self.height = height

  def draw(self):
    #TODO MAGIC NUMBER
    self.draw_line(self.color,(self.x,self.y),(self.x,self.y+self.height),5)
    self.draw_line(self.color,(self.x+self.width,self.y),(self.x+self.width,self.y+self.height),5)
    self.draw_line(self.color,(self.x,self.y_self,height),(self.x+self.width,self.y+self.height),5)
