import numpy as np

a_matrix = np.matrix([[1, 2], [3, 4]])
print(a_matrix)
# [[1 2]
#  [3 4]]

# modify a single item
a_matrix[1, 0] = 10
print(a_matrix)
# [[ 1  2]
#  [10  4]]

# modify an entire row
a_matrix[0] = [6, 3]
print(a_matrix)
# [[ 6  3]
#  [10  4]]

# sort
# sorts items in each row while leaving rows in same order
print(np.sort(a_matrix))
# [[ 3  6]
#  [ 4 10]]
print(-np.sort(-a_matrix))
# [[ 6  3]
#  [10  4]]

# transposing
# turns rows into columns and columns into rows via a pivot
a_matrix = np.matrix([[1, 2], [3, 4]])
print(a_matrix)
print(a_matrix.T)
# [[1 2]
#  [3 4]]
# [[1 3]
#  [2 4]]

# flatten
print(a_matrix.flatten())
# [[1 2 3 4]]


print(a_matrix * 2)
# or
# when adding be sure that the 2 argument matrices are the same shape
print(np.add(a_matrix, a_matrix))
# [[2 4]
#  [6 8]]

# matrix multiplication
print(np.matmul(a_matrix, a_matrix))
# [[ 7 10]
#  [15 22]]



