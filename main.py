import pygame 

#calendar class


#calendar class init
pygame.init()
screen_resolution = (800,600)
game_display = pygame.display.set_mode(screen_resolution)
pygame.display.set_caption('calendar')
clock = pygame.time.Clock()

#Main colors, these are shortcuts for easy colors
BLACK  = (0  ,0  ,0  )
RED    = (255,0  ,0  )
GREEN  = (0  ,255,0  )
BLUE   = (0  ,0  ,255)
PURPLE = (255,0  ,255)
YELLOW = (255,255,0  )
CYAN   = (0  ,255,255)
WHITE  = (255,255,255)


def draw_line(color,first,last,width=1):
  pygame.draw.line(game_display,color,first,last,width)


#calendar class update sceen
def update_screen():
  #  pygame.draw.line(game_display, (0,0,0),True,[(0,0),(screen_resolution)],1)
  pygame.draw.line(game_display,WHITE, (0,0),screen_resolution,1)
  pygame.display.update()
#

#logic loop
running = True
while running:
  for event in pygame.event.get():
    if event.type is pygame.QUIT:
      running = False
    #print event
    update_screen()
    clock.tick(60)
pygame.quit()
