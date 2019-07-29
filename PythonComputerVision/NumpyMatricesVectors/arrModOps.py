import numpy as np

an_arr = np.arange(0, 6)
print(an_arr)
# [0 1 2 3 4 5]

# Mod a single item at index
an_arr[0] = 10
print(an_arr)
# [10 1 2 3 4 5]

# reset
an_arr = np.arange(0, 6)

# insert
print(np.insert(an_arr, 0, [10, 11]))
# [10 11 0 1 2 3 4 5]
print(np.insert(an_arr, 1, [10, 11]))
# [ 0 10 11 1 2 3 4 5]

# append
print(np.append(an_arr, 6))
# [0 1 2 3 4 5 6]
print(np.append(an_arr, [6, 7]))
# [0 1 2 3 4 5 6 7]

# delete
print(np.delete(an_arr, 3))
# [0 1 2 4 5]

# mod every elem in array:
# multiply every elem
print(an_arr * 2)
print(an_arr + 2)
# [ 0  2  4  6  8 10]
# [2 3 4 5 6 7]
# etc

# sort:
# assending
another_arr = np.array([3, 6, 21, 9, 10, 1])
print(np.sort(another_arr))
# [ 1  3  6  9 10 21]
# decending
print(-np.sort(-another_arr))
# [21 10  9  6  3  1]


