# BOADCASTING
import numpy as np

# 2D array
## Rule 1. one of them have dimension size 1-> {(n,1),(1,m)}
# arr1 = np.array([[5],[2],[3],[4]])
# arr2 = np.array([[1,2,3,4]])
# arr2 = np.array([[5],[2],[3],[4]])

## Rule 2. dim have same size and 1 dim have size 1->{(n,1),(n,m)}
arr1 = np.array([[1],[2],[3],[4]])
arr2 = np.array([[1, 2, 3 ],
                 [5, 6, 7 ],
                 [9,10,11 ],
                 [13,14,15]])
print(arr1.shape)
print(arr2.shape)

print(arr1 * arr2)