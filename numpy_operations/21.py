# numpy slicing
import numpy as np

arr = np.array([
    #0, 1, 2, 3 column
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12],
    [13,14,15,16]
])
## array[start:end:step] 
# print(f"{arr[0:2]}\n")
# print(f"{arr[0:4:2]}\n")
# print(f"{arr[1:]}\n")
# print(f"{arr[::-2]}\n")
## print 1 - end
# print(f"{arr[1:]}\n")



# arr[row,column]
# print first column of every layer
# print(arr[:,0])

# second column
# print(arr[:,1])



# print all column
# print(arr[:,0:4])
# leave first column
# print(arr[:,1:])

# take every second column
# print(arr[:,0:4:2]) # can also be writen as arr[:,::2]

# print(arr[:,1:4:2])

# this will print column in reverse order
# print(arr[:,::-2])

# we want to do operation on selected rows and column

# print(arr[0:2,0:])
# print(arr[2:,0:2])





# print(type(arr))
# print(arr.ndim)
# print(arr.shape)