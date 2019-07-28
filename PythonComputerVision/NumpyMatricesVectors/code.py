# Creating Numpy Arrays

import numpy as np

list_1 = [1,2,3]
numpy_1 = np.array(list_1)

print(numpy_1)
# [1 2 3]

zeros_arr = np.zeros(5)
print(zeros_arr)
# [0. 0. 0. 0. 0. 0.]

ones_arr = np.ones(5)
print(ones_arr)
# [1. 1. 1. 1. 1. 1.]

range_array_1 = np.arange(5)
print(range_array_1)
# [ 0 1 2 3 4]

range_array_2 = np.arange(5, 11)
print(range_array_2)
# [ 5 6 7 8 9 10]

range_array_3 = np.arange(0, 20, 2)
print(range_array_3)
# [ 0 2 4 6 8 10 12 14 16 18]

linspace_array = np.linspace(0, 10, 5)
print(linspace_array)
# [ 0. 2.5 5. 7.5 10.]



