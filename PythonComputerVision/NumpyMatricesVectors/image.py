# Matrices by example
import numpy as np

# here each item represents a pixel in a square image and the numbers represent either black (1) or white (0)
image_matrix = np.matrix([[0, 0, 1, 0, 0],[0, 0, 1, 0, 0],[1, 1, 1, 1, 1],[0, 0, 1, 0, 0],[0, 0, 1, 0, 0]])
print(image_matrix)
# [[0 0 1 0 0]
#  [0 0 1 0 0]
#  [1 1 1 1 1]
#  [0 0 1 0 0]
#  [0 0 1 0 0]]

# flip white to balck and black to white
# first, find the boundaries assuming we might not be able to tell just by looking
rows = image_matrix.shape[0]
columns = image_matrix.shape[1]
print(rows)
print(columns)
# 5
# 5

# second, iterate through the rows and columns using a nested for loop
for row in range(rows):
  for column in range(columns):
    # check 0 or 1 and switch
    if image_matrix[row, column] == 0:
      image_matrix[row, column] = 1
    else:
      image_matrix[row, column] = 0

print(image_matrix)
# [[1 1 0 1 1]
#  [1 1 0 1 1]
#  [0 0 0 0 0]
#  [1 1 0 1 1]
#  [1 1 0 1 1]]

# rotate
image_matrix = np.matrix([[0, 0, 1, 0, 0],[0, 0, 1, 0, 0],[0, 0, 1, 0, 0],[0, 0, 1, 0, 0],[0, 0, 1, 0, 0]])
print(image_matrix)
# [[0 0 1 0 0]
#  [0 0 1 0 0]
#  [0 0 1 0 0]
#  [0 0 1 0 0]
#  [0 0 1 0 0]]

print(image_matrix.T)
# [[0 0 0 0 0]
#  [0 0 0 0 0]
#  [1 1 1 1 1]
#  [0 0 0 0 0]
#  [0 0 0 0 0]]

print(image_matrix.flatten())
# [[0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0]]


