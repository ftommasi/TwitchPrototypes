import pygame 

#TODO this probably isnt robust/general enough
#TODO this only works as a struct. Probably should add vector based movement 
#        (should it be internal to entities or should there be an exernal class)
#TODO add support for sprite/texture mapping
class Entity:
  def __init__(self,x,y,color):
    self.x = x
    self.y = y
    self.color = color

class Ball(Entity):
  def __init__(self,x,y,color,size):
    Entity.__init__(self,x,y,color)
    self.size = size
  def draw(self):
    draw_circle(self.color,self.x,self.y,self.size)

#TODO tweak with default values for w/h on net
#TODO net should never be smaller than balls
class Net(Entity):
  def __init__(self,x,y,color,width=50,height=50):
    Entity.__init__(self,x,y,color)
    self.width = width
    self.height = height
  def draw(self):
    draw_line(self.color,(self.x,self.y),(self.x,self.y+self.height))
    draw_line(self.color,(self.x+self.width,self.y),(self.x+self.width,self.y+self.height))



pygame.init()
screen_resolution = (800,600)
game_display = pygame.display.set_mode(screen_resolution)
pygame.display.set_caption('Basketball - Break In Progress...')
clock = pygame.time.Clock()
entities = []


#Main colors, these are shortcuts for easy colors
BLACK  = (0  ,0  ,0  )
RED    = (255,0  ,0  )
GREEN  = (0  ,255,0  )
BLUE   = (0  ,0  ,255)
PURPLE = (255,0  ,255)
YELLOW = (255,255,0  )
CYAN   = (0  ,255,255)
WHITE  = (255,255,255)


#entities 
ball = Ball(0,0,GREEN,40)
net = Net(10,10,RED)

entities += [ball,net]
def draw_line(color,first,last,width=1):
  pygame.draw.line(game_display,color,first,last,width)

def draw_circle(color,x,y,radius):
  pygame.draw.ellipse(game_display, color,(x,y,x+(2*radius),y+(2*radius)))

def update_screen():
  #update background
  draw_line(WHITE, (0,0),screen_resolution)
  #update entities
  for entity in entities:
    entity.draw()
  #update foreground

  #render to display
  pygame.display.update()

running = True
while running:
  for event in pygame.event.get():
    if event.type is pygame.QUIT:
      running = False
    #print event
    update_screen()
    clock.tick(60)
pygame.quit()
