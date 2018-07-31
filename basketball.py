import pygame

pygame.init()


def drawline(color,first,last,width=1):
  pygame.draw.line(game_display,color,first,last,width)

game_display = pygame.display.set_mode((800,600))
pygame.display.set_caption('Break in Progress...`')
clock = pygame.time.Clock()
running = True
while running:
  for event in pygame.event.get():
    if event.type is pygame.QUIT:
      running = False
    print event
  pygame.display.update()
  clock.tick(60)
pygame.quit()
