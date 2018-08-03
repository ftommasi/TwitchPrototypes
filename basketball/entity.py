import pygame

#TODO this probably needs to be more robust/generic
#TODO add support for sprite and texture mapping
#TODO implement more robust physics library
class Entity:
  def _init__ (self,x,y,color,priority,game_display):
    self.x = x
    self.y = y
    #self.pos = (self.x,self.y)?

    self.xvel = 0
    self.yvel = 0
    #self.vel_vec = (self.xvel,self.yvel)?

    self.xaccel = 0
    self.yaccel = 0
    #self.accel_vec = (self.xaccel,self.yaccel)?

    self.color = color
    #self.body = PhysicsRigidBody()

    #TODO would it make sense to do this? 
    #self.center_x = self.x/2.0
    #self.center_y = self.x/2.0
    #self.center = (self.center_x,self.center_y)

    #TODO: is this the best way to generalize this?
    self.game_display = game_display

  def update():
    pass
    #throw new MethodNotImplementedError("Entity child class not fully implemented")
  def draw():
    pass
    #throw new MethodNotImplementedError("Entity child class not fully implemented")

