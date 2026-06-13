# Scaler arithmetic - scalar is linear algebra term which means single values.
# When perform arithmetci operation between numpy array and scalar , operation is 
# applied to every element of the array.

import numpy as np

# arr = np.array([1,2,3])
# print(arr + 1)
# print(arr - 2)
# print(arr * 5)
# print(arr / 4)
# print(arr ** 3)

## Vectorized math function - linear algebra term , vector is an 1D list

# vec = np.array([1.6,2.55,3.4])

# print(np.sqrt(vec))
# print(np.floor(vec))


## EXERCISE

radi = np.array([2,3,4])
area = np.pi * radi **2

for i in range(len(area)):
    print(f"area of circle for radius ({radi[i]}) = {area[i]}")