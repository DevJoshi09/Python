## ELEMENT-WISE OPERATIONS

import numpy as np

# arr1 = np.array([1,2,3])
# arr2 = np.array([5,4,6])

# print(arr1 + arr2)

##  COMPARISON OPERATOR
score = np.array([10,20,33,66,78,100,11,111])

print(score < 100)

score[score<60] = 0
print (score)
