import pygame 

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
#TODO this only works as a struct. Probably should add vector based movement 
#        (should it be internal to entities or should there be an exernal class)
#TODO add support for sprite/texture mapping
class Entity:
  def __init__(self,x,y,color,priority):
    self.x = x
    self.y = y
    #entities are stationary by default
    self.dx = 0
    self.dy = 0
    self.color = color

  def update(self):
    self.x += self.dx
    self.y += self.dy
    
    
    #newdx = self.dx - 1
    #newdy = self.dy - 1
    #self.dx = newdx if newdx > 0 else 0
    #self.dy = newdy if newdy > 0 else 0

#TODO remove priority hard coded number from init
#TODO change 'physics' to a pos, velocity, acceleration system to avoid stupidity
class Ball(Entity):
  def __init__(self,x,y,color,size):
    Entity.__init__(self,x,y,color,1)
    self.size = size
  def draw(self):
    draw_circle(self.color,self.x,self.y,self.size)
  def update(self):
    Entity.update(self)
    if self.x + self.size >= screen_resolution[0] or self.x <= 0:
      self.dx *= -1
    if self.y <= 0 or self.y + self.size >= screen_resolution[1]:
      self.dy *= -1

#TODO tweak with default values for w/h on net
#TODO net should never be smaller than balls
#TODO remove priority hard coded number from init
class Net(Entity):
  def __init__(self,x,y,color,width=50,height=50):
    Entity.__init__(self,x,y,color,0)
    self.width = width
    self.height = height
  def draw(self):
    draw_line(self.color,(self.x,self.y),(self.x,self.y+self.height),20)
    draw_line(self.color,(self.x+self.width,self.y),(self.x+self.width,self.y+self.height),20)



pygame.init()
screen_resolution = (800,600)
game_display = pygame.display.set_mode(screen_resolution)
game_display.fill(WHITE)
pygame.display.set_caption('Basketball - Break In Progress...')
clock = pygame.time.Clock()
entities = []



#entities 
ball = Ball(0,0,GREEN,40)
net = Net(10,10,BLUE)

entities += [ball,net]

ball.dx = 10
ball.dy = 10
def draw_line(color,first,last,width=1):
  pygame.draw.line(game_display,color,first,last,width)


#NOTE: The way the draw works is (x,y,xlen,ylen) 
#       as opposed to (x1,y1,x2,y2)
#       this means that drawing anything like (x,y, x+r, y+r) 
#       makes the object grow as its position changes
def draw_circle(color,x,y,radius):
  pygame.draw.ellipse(game_display, color,(x,y,radius,radius))


event_count = 0
def update_screen():
  #update background
  #we draw this background every time because if not we get the [[[[[[[[[[[] overlap effect
  pygame.draw.rect(game_display,WHITE,(0,0,screen_resolution[0],screen_resolution[1]))
  #update entities
  #we do two for loops like this 
  #newcolor = tuple(map(lambda x : x + 20, ball.color))
  for entity in entities:
    entity.update()
  newdy = (ball.dy + 1.2)*ball.dy
  ball.dy = newdy if newdy < 50 else 50
  if ball.dy >= 10 and ball.y + ball.size >= screen_resolution[1] - 20:
    ball.y = screen_resolution[1] - ball.size -10
    ball.dy = 0
  for entity in entities:
    entity.draw()
  #update foreground

  #render to display
  pygame.display.flip()

running = True
while running:
  for event in pygame.event.get():
    if event.type is pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        running = False
    #print event
  update_screen()
  clock.tick(60)
pygame.quit()
