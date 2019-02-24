# Pygame dev 1
# basic game setup - display

import pygame


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Crossy RPG'
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
clock = pygame.time.Clock()

# Pygame dev 4
# Making code Obj Oriented with classes and objects

class Game:
  TICK_RATE = 60
  # FPS Frames Per Second

  def __init__(self, title, width, height):
    self.title = title
    self.width = width
    self.height = height

    self.game_screen = pygame.display.set_mode((width, height))
    self.game_screen.fill(WHITE_COLOR)
    pygame.display.set_caption(title)

  def run_game_loop(self):
    is_game_over = False
    direction = 0

    player_character = PlayerCharacter('player.png', 375, 700, 50, 50)
    # Pygame dev 2
    # set up the game loop to render graphics

    while not is_game_over:

      for event in pygame.event.get():

        if event.type == pygame.QUIT:
          is_game_over = True

        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP:
            print('K_UP')
            direction = 1
          elif event.key == pygame.K_DOWN:
            print('K_DOWN')
            direction = -1

        elif event.type == pygame.KEYUP:
          if event.key == pygame.K_UP or event.key ==pygame.K_DOWN:
            direction = 0

        # print(event)

      self.game_screen.fill(WHITE_COLOR)
      print('direction: ', direction)
      player_character.move(direction)
      player_character.draw(self.game_screen)

      pygame.display.update()
      clock.tick(self.TICK_RATE)

# Pygame dev 5
# Implement game classes - generic game obj class

class GameObject:

  def __init__(self, image_path, x, y, width, height):
    object_image = pygame.image.load(image_path)
    self.image = pygame.transform.scale(object_image, (width, height))

    self.x_pos = x
    self.y_pos = y
    self.width = width
    self.height = height

  def draw(self, background):
    background.blit(self.image, (self.x_pos, self.y_pos))

# Pygame dev 6
# Implement game classes - player character and movement

class PlayerCharacter(GameObject):

  SPEED = 10

  def __inti__(self, image_path, x, y, width, height):
    super().__init__(omage_path, x, y, width, height)

  def move(self, direction):
    if direction > 0:
      self.y_pos -= self.SPEED
    elif direction < 0:
      self.y_pos += self.SPEED


pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()


# Pygame dev 3
# Draw objects to screen and load imgs

# pygame.draw.rect(game_screen, BLACK_COLOR, [350, 350, 100, 100])
# pygame.draw.circle(game_screen, BLACK_COLOR, (400, 300), 50)

# player_image = pygame.image.load('player.png')
# player_image = pygame.transform.scale(player_image, (50, 50))
# game_screen.blit(player_image, (375, 375))

pygame.quit()
quit()



