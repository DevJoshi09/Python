# Numpy introduction 

import numpy as np
# print(np.__version__)


# arr = np.array([1,2,3,4])
# arr = arr * 2
# print(arr)
# print(type(arr))

arr = np.array([[['A','B','C'],['D','E','F'],['G','H','I']], #LAYER 0
                [['J','K','L'],['M','N','O'],['P','Q','R']], #LAYER 1
                [['S','T','U'],['V','W','X'],['Y','Z',' ']]  #LAYER 2
              ])

print(arr[0,0,0],arr[0,0,1],arr[1,1,1])

word = arr[0,0,0] + arr[2,0,0] + arr[2,0,0]

print(word)


