#Fausto Tommasi 2018

import pygame
from entity import *

#NOTE (... self.size)/2 is not a magic number it is by definition
#TODO maybe add an alias to self.size/2
class Ball(entity):
  def __init__(self,x,y,color,size,game_display):
    #TODO MAGIC NUMBER
    entity.__init__(self,x,y,color,1,game_display)
    #NOTE this is diameter not radius. It should also be renamed
    self.size = size 
    self.still_bouncing = True # do we even need this anymore?
    self.center_x = (self.x + self.size)/2
    self.center_y = (self.y + self.size)/2
  
  def draw(self):
    pygame.draw.ellipse(self.game_display,self.color,(self.x,self.y,self.size,self.size))

  #TODO: extrapolate these up to parent Entity class
  #NOTE we need this to update x,y and track center
  def update_x(self,newx):
    self.x += newx
    self.center_x = (self.y + self.size)/2
  
  #NOTE we need this to update x,y and track center
  def update_y(self,newy):
    self.y += newy
    self.center_y = (self.y + self.size)/2

  #TODO: fill in function stub??
  def update_pos(newpos):
    pass
    #self.update_x(newpos[0]) // self.update_x(newpos.x)
    #self.update_y(newpos[0]) // self.update_y(newpos.y)

  #TODO  properly implement delta usage instead of magic number
  def update(self,_delta):
    #delta = _delta
    #TODO MAGIC NUMBER
    delta = 1/10.0 #TODO what the fuck is with this magic number. RID OF IT ASAP
    self.update_x(self.xvel)
    self.update_y(self.yvel)
    self.xvel = (self.xaccel + self.xvel) * delta
    self.yvel = (self.yaccel + self.yvel) * delta

    #NOTE: acceleration of entity should bleed with friction
    #TODO: is this the right way of doing things?
    #TODO MAGIC NUMBER
    if self.xaccel < 0:
      self.xaccel += 0.03
    else:
      self.xaccel -= 0.03

    if abs(self.xaccel) < 0.2:
      self.xaccel = 0
    #TODO do we need this if check
    #TODO MAGIC NUMBER
    if self.still_bouncing:
      self.yaccel += 0.8

    #NOTE velocity caps
    #TODO: should we cap anything else (e.g. acceleration, pos, etc..)
    #TODO MAGIC NUMBER
    self.xvel = min(250,self.xvel)
    self.yvel = min(250,self.yvel)

    #NOTE scale down acceleration on collisions
    #TODO clean this up or refactor with physics
    #TODO move this logic to the drawing portion?
    if self.x + self.size >= self.screen_resolution or self.x <= 0:
      #TODO make this the normal perpendicular vector WRT walls instead
      self.xaccel *= -1
      #TODO: MAGIC NUMBER
      self.update_x(self.xaccel * 0.25)
    
    if self.y <= 0 or (self.y + self.size) >= self.screen_resolution[1]:
      self.yaccel *= -1
      #TODO MAGIC NUMBER
      self.update_y(self.yaccel*0.25)

      #TODO
      if abs(self.yaccel) < 13.75:
        self.yaccel = 0
        self.yvel = 0 
        self.still_bouncing = False
      else:
        #TODO MAGIC NUMBER
        self.yaccel = (((self.yaccel) - (0.1 * ((-1 * self.yaccel)/self.yaccel))) * 0.8)

