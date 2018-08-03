import pygame 
import math
import ball.py
import net.py

#Main colors, these are shortcuts for easy colors

BLACK  = (0  ,0  ,0  )
RED    = (255,0  ,0  )
GREEN  = (0  ,255,0  )
BLUE   = (0  ,0  ,255)
PURPLE = (255,0  ,255)
YELLOW = (255,255,0  )
CYAN   = (0  ,255,255)
WHITE  = (255,255,255)



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
