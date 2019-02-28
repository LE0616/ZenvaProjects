# Python laungage basics Part 3
# Collections
# Tuples, arrays/lists, dictionaries

width = 100
height = 200
# or
size = (100, 200)
width = size[0]
height = size[1]

new_size = size + (300,)
print(new_size)
# (100, 200, 300)
del new_size

len(size)
# 2
max(size)
# 200
min(size)
# 100
does_contain = 100 in size

print(does_contain)
# true

movement = [5, -2, -3, 4, -1]
first_movement = movement[0]
movement[0] = 7
# variable first_movement remains 5
movement.append(-5)
movement.remove(-3)

starting_positions = {'p_1': 50, 'p_2': 100, 'p_2': 150}
starting_positions['p_1']
starting_positions.keys()
starting_positions.values()

