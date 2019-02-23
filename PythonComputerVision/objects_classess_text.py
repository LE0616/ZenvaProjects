# Python language basics Part 7
# Classes and Objects
# Class fields, methos, and constructors
# Object instantiation

# Python isn't strictly object oriented but can be used well as such
# Python convention is to use _ as spaces in typical variables but Uppercase to start each word for classes
# "self" below refers to the class itself and is needed to define variables
# def __init__ is the constructor
# move() is a method

class GameCharacter:

  speed = 5

  def __init__(self, name, width, height, x_pos, y_pos):
    self.name = name
    self.width = width
    self.height = height
    self.x_pos = x_pos
    self.y_pos = y_pos

  def move(self, by_x_amt, by_y_amt):
    self.x_pos += by_x_amt
    self.y_pos += by_y_amt


char_0 = GameCharacter('char_0', 50, 100, 100, 100)
print(char_0.height)
char_0.name = 'Charlie'
print(char_0.name)

char_0.move(50, 100)
print('X', char_0.x_pos)
print('Y', char_0.y_pos)


# Python language basics Part 8
# Subclasses, superclasses, and inheritance

# Subclasses inherit from superclasses

class PlayerCharacter(GameCharacter):

  speed = 10

  def __init__(self, name, x_pos, y_pos):
    super().__init__(name, 100, 100, x_pos, y_pos)

  def move(self, by_y_amount):
    # self.y_pos =+ by_y_amount would override the superclasses move method entirely
    super().move(0, by_y_amount)


player_character = PlayerCharacter('p_char', 500, 500)
print(player_character.name)
player_character.move(100)
print(player_character.x_pos)
print(player_character.y_pos)





