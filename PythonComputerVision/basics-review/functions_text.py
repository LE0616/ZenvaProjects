# Python language basics Part 6
# Functions
# Implementing, calling, parameters, return values

x_pos = 0
e_x_pos = 4
print(x_pos)

# In Python a locally scoped variable must be tied to the global variable with a local variable call using the "global" keyword. If this is not done while the names may be the same the variable inside the fx only references within the fx scope and never touches the desired global variable. They are seen as 2 completely different variables, one that exists outside the fx and one that exists inside it.

def movefx():
  global x_pos
  x_pos += 1

movefx()

def move_by(amount):
  global x_pos
  x_pos += amount

move_by(3)


def check_for_collision():
  global x_pos
  global e_x_pos
  if x_pos == e_x_pos:
    return True
  else:
    return False

did_collide = check_for_collision()
print(x_pos)
print(did_collide)



