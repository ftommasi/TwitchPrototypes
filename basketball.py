import pygame 
import math

#Main colors, these are shortcuts for easy colors

BLACK  = (0  ,0  ,0  )
RED    = (255,0  ,0  )
GREEN  = (0  ,255,0  )
BLUE   = (0  ,0  ,255)
PURPLE = (255,0  ,255)
YELLOW = (255,255,0  )
CYAN   = (0  ,255,255)
WHITE  = (255,255,255)


#TODO this probably isnt robust/general enough
#TODO add support for sprite/texture mapping
#NOTE Physics formulae:
#       vel = dx/dt = (x2-x1)/(t2-t1) // v = a*t + v_0
#       accel = dv/dt = (v2-v1)/(t2-t1)

class Entity:
  def __init__(self,x,y,color,priority):
    self.x = x
    self.y = y
    self.pos = (self.x,self.y)
    self.xvel = 0 
    self.yvel = 0
    self.xaccel = 0
    self.yaccel = 0
    self.xdirection = 1
    self.ydirection = -1
    self.color = color

  def update(self,delta):
    pass



#TODO remove priority hard coded number from init
#TODO change 'physics' to a pos, velocity, acceleration system to avoid stupidity
class Ball(Entity):
  def __init__(self,x,y,color,size):
    Entity.__init__(self,x,y,color,1)
    self.size = size
    self.still_bouncing = True 
    self.center_x = self.x + size/2
    self.center_y = self.y + size/2

  def draw(self):
    draw_circle(self.color,self.x,self.y,self.size)
    draw_circle(RED,self.center_x,self.center_y,5)
    draw_circle(RED,self.center_x+(self.size/2),self.center_y,5)

 #TODO should these updates be += or just = and do the addition outside the function??
  def update_x(self,newx):
    self.x += newx
    self.center_x = self.x + self.size/2
  def update_y(self,newy):
    self.y += newy
    self.center_y = self.y + self.size/2
 
  def update(self,_delta):  
    #delta = _delta #
    delta = 1/10.0 #TODO what is this, we should maybe be passing a delta of time through fns
    friction = -0.3 #TODO how fast should acceleration bleed by
    gravity = 1.4
    self.update_x(self.xvel)
    self.update_y(self.yvel)
    self.xvel = (self.xaccel + self.xvel) *  delta
    self.yvel = (self.yaccel + self.yvel) *  delta
    if self.xaccel < 0:
      self.xaccel += 0.03  
    else:
      self.xaccel -=0.03


    if abs(self.xaccel) < 0.2:
      self.xaccel = 0
    if self.still_bouncing:
      self.yaccel += 0.8 
    
    #set movement caps
    self.xvel = min(250,self.xvel)     
    self.yvel = min(250,self.yvel)     

    #scale down accel vectors on collisions
    if self.x + self.size >= screen_resolution[0] or self.x <= 0:
      self.xaccel *= -1
      self.update_x(self.xaccel * 0.25)
      self.xaccel = (((self.xaccel) - (((-1 * self.xaccel)/self.xaccel))) * 0.8) 
    if self.y <= 0 or (self.y + self.size) >= screen_resolution[1]:
      self.yaccel *= -1
      self.update_y(self.yaccel * 0.25)
      #self.yaccel = (((self.yaccel) - (0.1 * ((-1 * self.yaccel)/self.yaccel))) * 0.8) 
      #print "~~checking for deactivation {}({})".format(self.yaccel,abs(self.yaccel))
      if abs(self.yaccel) < 13.75:
        #print "---DEACTIVATING---"
        self.yaccel = 0
        self.yvel = 0
        self.still_bouncing = False
      else:
        self.yaccel = (((self.yaccel) - (0.1 * ((-1 * self.yaccel)/self.yaccel))) * 0.8) 
      def debug_print():
        print "x: {}  y: {}".format(self.x,self.y)
        print "xvel: {}  yvel: {}".format(self.xvel,self.yvel)
        print "xaccell: {}  yaccel: {} ({})".format(self.xaccel,self.yaccel,abs(self.yaccel))
        #print "xdirecton: {}  ydirection: {}".format(self.xdirection,self.ydirection)
      #debug_print()


    #NOTE optimize by squaring both sides instead of sqrt    
    def is_point_colliding(self,point):
      if (
            (point[0] **2 <= (abs(self.size-((self.center_y + self.size) ** 2)))) and 
            (point[1] <= sqrt(abs(self.size-((self.center_x + self.size) ** 2)))**2)
         ):
        return True
      return False



#TODO tweak with default values for w/h on net
#TODO net should never be smaller than balls
#TODO remove priority hard coded number from init //Really think about needing this or not
class Net(Entity):
  def __init__(self,x,y,color,width=50,height=50):
    Entity.__init__(self,x,y,color,0)
    self.width = width
    self.height = height
  def draw(self):
    draw_line(self.color,(self.x,self.y),(self.x,self.y+self.height),5)
    draw_line(self.color,(self.x+self.width,self.y),(self.x+self.width,self.y+self.height),5)
    draw_line(self.color,(self.x,self.y+self.height),(self.x+self.width,self.y+self.height),5)
    draw_circle(RED,self.x,self.y,5)

  def is_point_colliding(self,point):
    pass
    if (
          (point[0] > self.x and point[0] < self.x + 5) or (point[0] > self.width and point[0] < self.width + 5) and 
          (point[1] > self.y and point[1] < self.height) or (point[1] < self.height+5 and point[1] > self.height)
       ):
      pass


pygame.init()
screen_resolution = (800,600)
game_display = pygame.display.set_mode(screen_resolution)
game_display.fill(WHITE)
pygame.display.set_caption('Basketball - Break In Progress...')
clock = pygame.time.Clock()
entities = []

mode = {}

#entities 
mode["left"] = Ball(170,300,GREEN,40)
mode["right"] = Ball(530,300,YELLOW,40)
mode["top"] = Ball(330,150,BLACK,40)
mode["bot"] =  Ball(330,350,(125,255,70),40)
net = Net(300,300,BLUE,100)

mode["left"].xaccel = 70
mode["left"].yaccel = 0
mode["right"].xaccel = -70
mode["right"].yaccel = 0
mode["top"].xaccel = 0
mode["top"].yaccel = 10
mode["bot"].xaccel = 0
mode["bot"].yaccel = -50

ball = mode["top"]

entities += [ball,net]

def draw_line(color,first,last,width=1):
  pygame.draw.line(game_display,color,first,last,width)


#NOTE: The way the draw works is (x,y,xlen,ylen) 
#       as opposed to (x1,y1,x2,y2)
#       this means that drawing anything like (x,y, x+r, y+r) 
#       makes the object grow as its position changes
def draw_circle(color,x,y,radius):
  pygame.draw.ellipse(game_display, color,(x,y,radius,radius))
  

def calculate_distance(point1,point2):
  return math.sqrt(abs((point2[0]-point1[0]) + (point2[1] - point1[1])))


#NOTE potentialoptimization would be to divide the screen region
#   into 4 quadrants and only check the entities in each quadrannt. 
#   This divide and conquer would decrease the number of dumb collision checks
def update_collisions(entities,screen_region):
  for entity1 in entities:
    for entity2 in entities:
      if entity1 is entity2:
        continue
    #if calculate_distance((entity1.center_x,entity1.center_y),)
    pass

event_count = 0
def update_screen(delta):
  #update background
  #NOTE: we draw this background every time because if not we get the [[[[[[] overlap effect
  pygame.draw.rect(game_display,WHITE,(0,0,screen_resolution[0],screen_resolution[1]))
  #update entities
  #we do two for loops like this 
  for entity in entities:
    entity.update(delta)
  
  #update_collisions(entities,screen_resolution)
  #TODO: check if ball is colliding with basket. This will need to be refactored into something less crappy
  #      check if ball can go into bucket and cant 'phase' into it 
    #collision detected/ do something
    
  if (
        #TODO: add ball radius to collision detection
        ((ball.center_y < (net.height + net.y) and ball.center_y > net.y)) and (((net.x - 5) <= ball.center_x + (ball.size/2)) and (ball.center_x < net.x + 5)) or 
        ((ball.center_y < (net.height + net.y) and ball.center_y > net.y)) and (((net.x + net.width) >= ball.center_x - (ball.size/2)) and (ball.center_x > net.x + net.width - 5)) or
        ((ball.center_x < (net.width  + net.x) and ball.center_x > net.x)) and (((net.y + net.height) >= ball.center_y - (ball.size/2)) and (ball.center_y > net.y + net.height - 5)) 
     ):
  
    #HACK temp direction switch to verify other code
    #NOTE: Idea is to change velocity vector to vector perpendicular to current velocity vector with respect to the surface of the collision
    #print "~~net collision~~ at Ball ({},{}) with net(x:{} - w:{}, y: {} - h: {})".format(ball.center_x,ball.center_y,net.x,net.x+net.width,net.y,net.y+net.height)
    ball.xaccel *= -1
    ball.yaccel *= -1
    ball.x += ball.xaccel
    ball.y += ball.yaccel

  for entity in entities:
    entity.draw()
  #update foreground
  ball_center = (ball.center_x, ball.center_y)
  #render to display
  pygame.display.flip()

running = True
while running:
  time = pygame.time.Clock().get_rawtime()
  for event in pygame.event.get():
    if event.type is pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        running = False
    #print event
  update_screen(pygame.time.Clock().get_rawtime() - time)
  clock.tick(60)
pygame.quit()
