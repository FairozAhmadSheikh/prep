# 1. Create a 1D NumPy array with values from 0 to 9
import numpy as np
var=np.arange(0,10)
# print(var)

#  2. Create a 2D array with the following values: [123456789]
# ar2=np.arange(1,10).reshape(3,1,3)
# print(ar2)
# print(ar2.ndim)
# print(ar2.shape)

# ar3=np.array([[[1,2,3],
#                [4,5,6],
#                [7,8,9]]])
# print(ar3.ndim)

# 3. Create a 3D array of shape (3, 3, 3) filled with random integers between 0 and 10

# var4d=np.random.randint(0,11,(3,3,3))
# print(var4d)
# print(type(var4d))
# print(np.info(var4d))

# 4. Create a NumPy array of zeros with shape (4, 5) and another of ones with shape (3, 2)
# import numpy as np

# zer=np.zeros((4,5))
# print(zer)
# one=np.ones((3,2))
# print(one)

# Slicing and Indexing
# 1. From the 2D array, extract:
#    o The second row

# ar2=np.arange(0,10).reshape(2,5)
# # print(ar2.ndim)
# print(ar2)
# print(ar2[0:,-3])

# ar2=np.array([[1,2,3,4,5,6],
#               [7,8,9,6,5,4],
#               [3,2,3,5,7,8],
#               [4,5,7,8,9,6]
#               ])

# print(ar2[3:,2:4])
import numpy as np

var = np.array([
    [
    [3, 1, 2],
    [5, 2, 6],
    [3, 9, 1]],

   [[8, 3, 4],
    [1, 8, 9],
    [2, 5, 2]],

   [[3, 1, 8],
    [8, 1, 3],
    [9, 1, 1]]])

# o Extract the first 2D "slice" (along the first axis)
# print(var[1:2,0:,1:2])

#  o Extract a sub-array containing the first two rows and first two columns of the second 2D slice
# print(var[1:2,0:2,0:2])


# Broadcasting
# 1. Add 5 to each element of the 1D array
# 2. Multiply the 2D array by a scalar value (e.g., 2)
# 3. Create two arrays and add them using broadcasting

ar1=np.arange(1,11)
# print(ar1)

# 1. Add 5 to each element of the 1D array
new_arry=ar1+5
# print(new_arry)

# 2. Multiply the 2D array by a scalar value (e.g., 2)
new_arry=new_arry.reshape(2,5)
new_arry=new_arry*5
# print(new_arry)

# 3. Create two arrays and add them using broadcasting

arr1=np.random.randint(1,11,(3,4))
# print(arr1)
arr2=np.random.randint(20,31,(3,4))
# print(arr2)
arr3=arr1+arr2
# print(arr3)

# Manipulating 3D Arrays
# 1. Create a 3D array of shape (4, 4, 4) filled with random floating-point numbers between 0 and 1
ar3=np.random.random((4,4,4))
# print(ar3)

# sums=ar3.sum()
# print(sums)
# means=ar3.mean()
# print(means)

# cum_sum=ar3.cumsum()
# print(cum_sum)

# zarray=np.random.random((4,4))
# print(zarray)
