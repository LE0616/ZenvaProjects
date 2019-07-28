import numpy as np

an_arr = np.arange(0, 11)
print(an_arr)
# [ 0 1 2 3 4 5 6 7 8 9 10]

first_elem = an_arr[0]
print(first_elem)
last_elem = an_arr[10]
print(last_elem)
# 0
# 10

first_five = an_arr[0:5]
print(first_five)
# [0 1 2 3 4]
# same as
# first_five = an_arr[:5]

last_five = an_arr[6:]
# to the end
print(last_five)
# [ 6 7 8 9 10]

last_five_step = an_arr[6::2]
print(last_five_step)
# [ 6 8 10]

first_five_reversed = an_arr[4::-1]
print(first_five_reversed)
# [4 3 2 1 0]

final_two = an_arr[-2:]
print(final_two)
# [ 9 10]

# length
print(an_arr.size)

# max
print(np.amax(an_arr))

# min
print(np.amin(an_arr))

# average
print(np.average(an_arr))
