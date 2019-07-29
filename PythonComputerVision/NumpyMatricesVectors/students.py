# Arrays by Example
import numpy as np

student_grades = np.array([56, 78, 98, 90, 58, 64, 67, 72, 93, 51])
print(student_grades)
# [56 78 98 90 58 64 67 72 93 51]

class_average = np.average(student_grades)
print(class_average)
# 72.7

highest_grade = np.amax(student_grades)
print(highest_grade)
# 98

lowest_grade = np.amin(student_grades)
print(lowest_grade)
# 51

# indexes of
np.argmax(student_grades)
np.argmin(student_grades)
# 2
# 9

print(np.sort(student_grades))
print(-np.sort(-student_grades))
# [51 56 58 64 67 72 78 90 93 98]
# [98 93 90 78 72 67 64 58 56 51]

# increase 10%
increased_grades = student_grades * 1.1
print(increased_grades)
# [ 61.6  85.8 107.8  99.   63.8  70.4  73.7  79.2 102.3  56.1]

# increase 10 pts
increased_grades = student_grades + 10
print(increased_grades)
# [ 66  88 108 100  68  74  77  82 103  61]

# create and array with the same number of slots and add together the contents present at common indexes
print(np.add(student_grades, np.ones(10)))
print(np.add(student_grades, np.array([1, 2, 3, 4,5, 6, 7, 8, 9, 10])))
# [57. 79. 99. 91. 59. 65. 68. 73. 94. 52.]
# [ 57  80 101  94  63  70  74  80 102  61]

