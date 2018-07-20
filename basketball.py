import pygame

pygame.init()

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
