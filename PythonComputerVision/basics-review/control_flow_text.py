# Python language basics Part 4
# Control Flow
# if statements

# if condition:
#   code to execute if condition is true

is_game_over = False
p_0_x_pos = 0
e_0_x_pos = 3
e_1_x_pos = 5

p_0_x_pos += 2

if p_0_x_pos == e_0_x_pos:
  is_game_over = True
elif p_0_x_pos == e_1_x_pos:
  is_game_over = True
else:
  e_0_x_pos += 1
  e_1_x_pos += 1

# or

if p_0_x_pos == e_0_x_pos or p_0_x_pos == e_1_x_pos:
  # "and" opperator also used by spelling out "and" directly
  is_game_over = True
else:
  e_0_x_pos += 1
  e_1_x_pos += 1

  # note if indentation is not included the script will not run properly...in Python the : and indentation are a vital part of syntax

# Python language basics Part 4
# while loops
# for in loops

# while not is_game_over:
  # do something and loop until the while condition fails
  # look out for infinate loops!

is_game_over = False
p_x_pos = 0
e_x_pos = 3
end_x_pos = 10

while not is_game_over:
  print('Player: ', p_x_pos)
  print('Enemy: ', e_x_pos)

  if p_x_pos == e_x_pos:
    print('You Lose')
    is_game_over = True
  elif p_x_pos >= end_x_pos:
    print('You WIN')
    is_game_over = True
  else:
    p_x_pos += 3
    e_x_pos += 1

    # You WIN!

# again if you dont back ouyt of the tab used in the above else statement the code will be read as if below occurs inside that else....weird right!
x_pos = 5
movements = [1, -2, 6, -3, -2, 4]

# for each single element in this array
for movement in movements:
  x_pos += movement
print(x_pos)

