import numpy as np

two_by_two = np.matrix([[1, 2], [3, 4]])
print(two_by_two)
# [[1 2]
#  [3 4]]

two_by_three = np.matrix('1 2; 3 4; 5 6')
print(two_by_three)
# [[1 2]
#  [3 4]
#  [5 6]]

print(np.zeros([3, 2]))
# [[0. 0.]
#  [0. 0.]
#  [0. 0.]]
