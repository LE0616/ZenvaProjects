# Pygame dev 1
# basic game setup - display

import pygame



SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Crossy RPG'
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
YELLOW_COLOR = (255, 255, 0)
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('comicsans', 50)


# Pygame dev 4
# Making code Obj Oriented with classes and objects

class Game:
  TICK_RATE = 60
  # FPS Frames Per Second

  def __init__(self, image_path, sound_path, title, width, height):
    self.title = title
    self.width = width
    self.height = height

    self.game_screen = pygame.display.set_mode((width, height))
    self.game_screen.fill(WHITE_COLOR)
    pygame.display.set_caption(title)

    background_image = pygame.image.load(image_path)
    self.image = pygame.transform.scale(background_image, (width, height))

    # Pygame Dev EXTRA
    # Game Music
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play(-1)
    # sets music to auto-loop


  def run_game_loop(self, level_speed):
    is_game_over = False
    did_win = False
    direction = 0

    player_character = PlayerCharacter('player.png', 375, 700, 50, 50)
    enemy_0 = EnemyCharacter('enemy.png', 20, 400, 50, 50)
    enemy_0.SPEED *= level_speed

    enemy_1 = EnemyCharacter('enemy.png', self.width - 40, 600, 50, 50)
    enemy_1.SPEED *= level_speed

    enemy_2 = EnemyCharacter('enemy.png', self.width - 40, 200, 50, 50)
    enemy_2.SPEED *= level_speed

    treasure = GameObject('treasure.png', 375, 50, 50, 50)
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
      self.game_screen.blit(self.image, (0, 0))

      treasure.draw(self.game_screen)

      player_character.move(direction, self.height)
      player_character.draw(self.game_screen)

      enemy_0.move(self.width)
      enemy_0.draw(self.game_screen)

      # Pygame dev 10
      # Adding levels with inc. difficulty
      if level_speed > 2:
        enemy_1.move(self.width)
        enemy_1.draw(self.game_screen)
      if level_speed > 4:
        enemy_2.move(self.width)
        enemy_2.draw(self.game_screen)

      # Pygame dev 9
      # Add true end game conditions - win and lose
      if player_character.detect_collision(enemy_0) or player_character.detect_collision(enemy_1) or player_character.detect_collision(enemy_2):
        is_game_over = True
        did_win = False
        text = font.render('You SUCK! wah wah!', True, WHITE_COLOR)
        self.game_screen.blit(text, (220, 350))
        pygame.display.update()
        clock.tick(1)
        break
      elif player_character.detect_collision(treasure):
        is_game_over = True
        did_win = True
        text = font.render('Whoo, you rule BITCH!', True, WHITE_COLOR)
        self.game_screen.blit(text, (200, 350))
        pygame.display.update()
        clock.tick(1)
        break
      # Pygame has some really optimized collision fuctions on board you should use when you have many potential collisions to track

      pygame.display.update()
      clock.tick(self.TICK_RATE)

    if did_win:
      self.run_game_loop(level_speed + 0.5)
    else:
      return

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
    super().__init__(image_path, x, y, width, height)

  def move(self, direction, max_height):
    if direction > 0:
      self.y_pos -= self.SPEED
    elif direction < 0:
      self.y_pos += self.SPEED

    if self.y_pos >= max_height - 20:
      self.y_pos = max_height - 20

  # Pygame dev 8
  # Implement collision detection with enemies and treasure

  def detect_collision(self, other_body):
    if self.y_pos > other_body.y_pos + other_body.height:
      return False
    elif self.y_pos + self.height < other_body.y_pos:
      return False

    if self.x_pos > other_body.x_pos + other_body.width:
      return False
    elif self.x_pos + self.width < other_body.x_pos:
      return False

    return True

# Pygame dev 7
# Implement game classes - enemy character and bounds checking

class EnemyCharacter(GameObject):

  SPEED = 5

  def __inti__(self, image_path, x, y, width, height):
    super().__init__(image_path, x, y, width, height)

  def move(self, max_width):
    if self.x_pos <= 20:
      self.SPEED = abs(self.SPEED)
    elif self.x_pos >= max_width - 40:
      self.SPEED = -abs(self.SPEED)
    self.x_pos += self.SPEED

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

new_game = Game('background.png', 'PM_NIGHTPULSE_120BPM_06.mp3', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
# .wav file does not work...use MP3
new_game.run_game_loop(1)


# Pygame dev 3
# Draw objects to screen and load imgs

# pygame.draw.rect(game_screen, BLACK_COLOR, [350, 350, 100, 100])
# pygame.draw.circle(game_screen, BLACK_COLOR, (400, 300), 50)

# player_image = pygame.image.load('player.png')
# player_image = pygame.transform.scale(player_image, (50, 50))
# game_screen.blit(player_image, (375, 375))

pygame.quit()
quit()



