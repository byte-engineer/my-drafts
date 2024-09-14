# Draft/Librarys/Numpy.py

# General veiw------------------------------------------------------
#|> Numpy is very excellent for general-purpose scientific computing.
#|> Python comunity are using this module because of it's efficiency.
#|> Numpy is disgined to deal with numbers arrays.
#|> Numpy store the date in same resion in memory and dont use array of pionters as lists.

# Importing---------------------------------------------------------

import numpy as np                                               # Importing the module
np.__version__                                                   # Version => 1.26.4

# Array Creation----------------------------------------------------

#|> All elements of the array must be of the same type of data.
#|> Once created, the total size of the the array can’t change.
#|> The shape must be rectangular

ints  = np.array([1, 2, 3, 4, 5], dtype= "int16")                # Create an array contains an integers in 16 bit for every integer.
flts  = np.array([1, 2], dtype= "float32")                       # floats array.

# Array metodes-----------------------------------------------------



# Arays Opration----------------------------------------------------

arr1 = np.array([1,2,3,4,5 ], dtype= "float16", )
arr2 = np.array([10,9,8,7,6], dtype= "float16", )

arr1 + arr2
arr1 - arr2
arr1 * arr2
arr1 / arr2
arr1 % arr2
arr1 //arr2
arr1 **arr2

# Advanced oprations------------------------------------------------

MAT = np.array([[1, 2, 3],
                [4, 5, 6], 
                [7, 8, 9]])

vec = np.array([1, 2, 3])

print(np.matmul(vec, MAT))


