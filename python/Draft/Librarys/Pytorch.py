import os 
os.system("cls")
#-----------------------------------------------------------
#|> Pytorch is very populare library for AI & Deep learning.
#|> Colab is a great site to work with Pytorch.
#|> Pytorch supports accelirators like GPU and CPU

import torch

# We can Use this commend to get info a bout GPU in Colap  -> !nvidia-smi
print(torch.__version__)                         # Version --> 2.3.1+cpu
# Tensors---------------------------------------------------

scaler = torch.tensor(9)                                    # Create a Zero-dimensional tensor.

vector = torch.tensor([9., 3., 5., 6.])                     # Create a One-dimensional tensor.

matrix = torch.tensor([[9, 3, 5, 6],                        # Create a Two-dimensional tensor.
                       [3, 3, 6, 8],
                       [5, 6, 2, 0]])

tensor = torch.tensor([[[9, 3, 5, 6],                       # Create a Three-dimensional tensor.
                        [3, 3, 6, 8],
                        [5, 6, 2, 0]],

                       [[1, 6, 6, 3], 
                        [9, 3, 5, 6],
                        [3, 5, 6, 7]]])

# Tensor indexing-------------------------------------------

#|> Indexing in tensors is very similar to a numpy.
#|> Tensors are zero base indexed.
#|> We can use ":" to sellect "all" the elelment ofspcefic dimention
#|> We can use "," in stead of "[]" so this [1][2][0] is same [1, 2, 0]

# Indexing
vector[2]                                                   # Result => tensor(5)
vector[-1]                                                  # Result => tensor(6)
tensor[1][2]                                                # Result => tensor([3, 5, 6, 7])
tensor[1][2][0]                                             # Result => tensor(3)
matrix[:][1]                                                # Result => tensor([3, 3, 6, 8])

# slicing
vector[1:3]                                                 # Result => tensor([3, 5])
vector[::2]                                                 # Result => tensor([9, 5])

# Some Tensors attributes-----------------------------------

# We use .ndim method to get a number of dimension of a tensor
scaler.ndim                                                 # Result => 0
vector.ndim                                                 # Result => 1
matrix.ndim                                                 # Result => 2
tensor.ndim                                                 # Result => 3

# We use .shape method to get a shape of a tensor
scaler.shape                                                # Result => torch.Size([])
vector.shape                                                # Result => torch.Size([4])
matrix.shape                                                # Result => torch.Size([3, 4])
tensor.shape                                                # Result => torch.Size([2, 3, 4])

# Generate Tensors--------------------------------------------

#|> Very importent because are commonly used for to initaite a nural network.

data0 = torch.tensor([[2.3, 6.3],
                      [2.9, 3.1]])

seed = 42
torch.manual_seed(seed)                                     # Set a seed for reproducablety
# Create a random float 0-to-1 tensor
torch.rand(3, 4)                                            # 3-by-4 tensor contains random float values beteen Zero & One.torch.rand_like(data0)                                      # Random tensor in same shape of data0 which is 2x2

# Create a random integer tensor
torch.randint(0, 10, (3, 3, 3))                             # Creates a tensor contains a random integer values between 0, 10.

# Create One-&-Zeros tensor
torch.zeros(3, 3)                                           # Return => tensor([[0., 0., 0.],[0., 0., 0.],[0., 0., 0.]])
torch.ones(3, 3)                                            # Return => tensor([[1., 1., 1.],[1., 1., 1.],[1., 1., 1.]])

# Create arange Tensor torch(start, end, step)
torch.arange(0, 10, 2)                                      # Return => tensor([0, 2, 4, 6, 8])

# Tensor Date type------------------------------------------

#|> Using True data type almost make the code more eficiant.
#|> There are many Data type in pytorch like {int16, float32, uint64, ...}
#|> Default Data type in Pytorch is "float32"
#|> Pytorch is support three devices {"cpu", "cuda", "tpu"}
#|> We can't do an oprations between tow Tensors has defferant Device.

A = torch.tensor([1,2,3,4], dtype= torch.uint16 , device= "cpu")     # This will return unsigned(positive) 16-bit integers that can run in CPU.
B = torch.tensor([1,2,3,4], dtype= torch.float64, device= "cpu")     # This will return 64-bit float numbers that can run in CPU.

# get info a bout a tensor

A.dtype                        # Get the date type of a tensor. 
A.shape                        # get the shape of a tensor.
A.device                       # Get the device of a tensor.

# Tensors Oprations----------------------------------------

A = torch.tensor([1,2,3,4], dtype= torch.float64 , device= "cpu")
B = torch.tensor([5,6,7,8], dtype= torch.float64, device= "cpu")

A + B                # Addition
A - B                # Subtraction
A * B                # Mutiplication (element-wise)
A / B                # Division
A ** B               # Power
A %  B               # Modulus
A // B               # Floor division

# Matrex multiplication
# torch.matmul() Is such faster 8 times then do the code by python (for) loop.
# Also caled dot-product.
# [a, b, c] . [d, e, f]  = [a*d + b*e + c*f]

# RULES
# We will create an error if inner dimension not match. shape ->  ( 3 , {2}) @ ({2}, 3  ) 
# The resulting tensor will be shaped same as outer dimintion ->  ({4},  7 ) @ ( 7 ,{2} )  = (4, 2)


torch.matmul(A , B)       # Return [1*5 + 2*5 + 3*6 + 4*7] = tensor(70)
A @ B                     # Other syntax.

# Transpose
# Is swich the axes of a given tensor.
matrix.T                # Return the trensposed version of MATREX.

# tensor aggregation-----------------------------------------------

# Finding min, max, mean, sum, etc...

some_tensor = torch.rand((24))*10

# Find the min & max
torch.min(A), A.min()                # Return a scaler tensor containing a minimam value.
torch.max(A), A.max()                # Return a scaler tensor containing a maximam value.

# Find the mean (average)            # Tensor must be on a float data type
torch.mean(A), A.mean()              # Returns the mean of A

# Find the sum
torch.sum(A), A.sum()                # Return the sum

# Reshape                                       # the resized tensor must contain the same number of elements.
C = torch.reshape(some_tensor, (3, 4, 2))       # The new tensor shape => (3, 4, 2) which contains same number of elementes.

# Stack
# Stacks a on top of each other
torch.stack((A, B), dim=0)                      # Stack A on B

# Squeeze & Unsqueeze                               # Add and remove a singel dimenion
D = torch.squeeze(A, dim= 0)                        # Return => tensor([[1,2,3,4]])
torch.unsqueeze(D, dim= 0)                          # Return => tensor([1,2,3,4])

image = torch.rand(144, 144, 3) # ==> (hieght, width, colours)

# Premute
# It share same memory addresses as oregnal tensor.
# rearange dimension to a certain way.
torch.permute(image, (2, 0, 1))     # Return a dimension in this arrangment (colours, hieght, width)

# flatten 
# Convert a tensor to a single dimension
image.flatten(), torch.flatten(image)

# Pytorch and Numpy-------------------------------------------------

#|> Pytorch is compatable with numpy 
#|> We can convert torch tensors to numpydata arrays and backward

import numpy as np
array = np.array([12, 12, 56, 62])

torch.from_numpy(array)                          # Convert NDarray(numpy array) to a tensor
torch.Tensor.numpy(A)                            # Convert a Tensor to a numpy array.

# GPUs--------------------------------------------------------------

torch.cuda.is_available()        # Return True if available
torch.cuda.device_count()        # Return a number of GPUs

