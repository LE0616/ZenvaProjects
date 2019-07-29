import numpy as np

a_matrix = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a_matrix)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# row
print(a_matrix[0])
# [[1 2 3]]

# specific item or items x = row index y = column index
print(a_matrix[1, 0])
# 4
print(a_matrix[2, 1:3])
# [[8 9]]

# total number of items
print(a_matrix.size)
# 9

# shape
print(a_matrix.shape)
# (3, 3)

print(np.amax(a_matrix))
print(np.amin(a_matrix))
print(np.average(a_matrix))
# 9
# 1
# 5.0

print(a_matrix.max())
print(a_matrix.min())
print(a_matrix.mean())
# 9
# 1
# 5.0

