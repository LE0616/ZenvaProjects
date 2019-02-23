# Pygame dev 1
# basic game setup - display

import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Crossy RPG'
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
clock = pygame.time.Clock()
TICK_RATE = 60
# FPS Frames Per Second
is_game_over = False

game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_screen.fill(WHITE_COLOR)
pygame.display.set_caption(SCREEN_TITLE)

player_image = pygame.image.load('player.png')
player_image = pygame.transform.scale(player_image, (50, 50))

# Pygame dev 2
# set up the game loop to render graphics

while not is_game_over:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      is_game_over = True

    print(event)
  # Pygame dev 3
  # Draw objects to screen and load imgs
  # pygame.draw.rect(game_screen, BLACK_COLOR, [350, 350, 100, 100])
  # pygame.draw.circle(game_screen, BLACK_COLOR, (400, 300), 50)

  game_screen.blit(player_image, (375, 375))

  pygame.display.update()
  clock.tick(TICK_RATE)

pygame.quit()
quit()



