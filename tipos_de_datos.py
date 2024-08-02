import numpy as np

###### Create an array ######

# arr = np.array([1,2,3,4])
# print(arr)

###### Check data type ######

# print(arr.dtype)

###### Create the array with different data type ######

# arr = np.array([1,2,3,4], dtype='float64')
# print(arr)
# print(arr.dtype)

###### Change data type ######

# arr = np.array([1,2,3,4])
# print(arr)

# arr = arr.astype(np.float64)
# print(arr)

###### Bool data type, when a value is zero, it returns false ######

# arr = np.array([0,1,2,3,4])
# arr = arr.astype(np.bool_)
# print(arr)

###### String data type change ######

# arr = np.array([0,1,2,3,4])
# arr = arr.astype(np.str_)
# print(arr)

###### Int data type

arr = np.array(['0','1','2','3 ','4'])
arr = arr.astype(np.int8)
print(arr)