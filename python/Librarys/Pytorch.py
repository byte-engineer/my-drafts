# Draft/Librarys/Pytorch.py

import os 
os.system("cls")
#-----------------------------------------------------------
#|> Pytorch is very populare library for AI & Deep learning.
#|> Colab is a great site to work with Pytorch.
#|> Pytorch supports accelirators like GPU and CPU

import torch

# We can Use this commend to get info a bout GPU in Colap  -> !nvidia-smi
print(torch.__version__)                         # Version --> 2.3.1+cpu
input("finish importing...\nPress Any key...")


# BASICS #
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

torch.randn(1)                                              # Create a random number from 0 to 1

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

# get info a bout a tensor.

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

torch.from_numpy(array)                          # Convert NDarray(numpy array) to a tensor.
torch.Tensor.numpy(A)                            # Convert a Tensor to a numpy array.

# GPUs & Accelerators-----------------------------------------------
#|> Run the calclations on a GPU or a TPU is faster several times.
#|> I  Don't have a GPU ):
#|> I can use other online GPUs and TPUs providers like: Colab, kaggle

torch.cuda.is_available()          # Return True if available.     |Output => False
torch.cuda.device_count()          # Return a number of GPUs.      |Output => 0
# torch.cuda.get_device_name()     # Return the device name.       |Will raise error

# Ignostic-Device
Device = 'cuda' if torch.cuda.is_available() else 'cpu'

# =================================================================================================
#### WORK FLOW=====================================================================================
# =================================================================================================


#|> Steps:
#   * Get data ready.
#   * Build or pick a model.
#   * Fit the model into our data.
#   * Evaluat our model.
#   * Experimentation and improve.
#   * Save and relaod our trained model. 

#|> Data can be anything in machine learning.
#   * Text
#   * Audio
#   * Vedio
#   * Other...


#|> Becase We will convert our Data in numerical representation.
#|> Then we will search a pattrens in that numerical representation in some way.
#|> NN stands for Neural Network which is the smallest building block in machine learning.
#|> We can create a fake data for educational porposes.

### First model----------------------------------------------------------------------------------------------


##  Data ready

# Create *known* parameters       # In almost situations we don't know the values of this parameters.
weight = 0.7                      # This is random parameters
bias = 0.3                        # This also

x = torch.arange(0, 1, 0.02).unsqueeze(dim=1)   # Unsqueese to add inner dimension # lengh of x is 50 and it's shape is 50, 1
y = weight * x + bias                           # line equation 


# First we have to split the data to for training data and testing data.
split_border = int(0.8 * len(x))                          # The splitting border.

xtrain, ytrain = x[:split_border], y[:split_border]
xtest, ytest   = x[split_border:], y[split_border:] 


# Our first model in pytorch.
#|> Our gole is to find our known weight & bias with out give it to the NN dirctly.
#|> We will create a class Inherits from torch.nn module.
#|> NN module deal with almost functions we need to create our model.
#|> Our class should be sub-class of torch.nn.Module.
#|> When we sub-class torch.nn.Module We should over-write "forword()"
#|> That method defines the forword computation.


class LRM(torch.nn.Module):  # LinearRegressionModel


    def __init__(self) -> None:
        super().__init__()
        
        # Create and initlaize our parameters with random parameters.  # We can initlize with zeroes or a numbers from other models.
        self.weight = torch.nn.Parameter(torch.randn(1,                      # our Weight as a Parameter 
                                               requires_grad= True,    # This option enabled, it trace our weight when we applay any opration.
                                               dtype= torch.float32))  # This the default option.

        self.bias   = torch.nn.Parameter(torch.randn(1,                    # our Bias as a Parameter
                                               requires_grad= True,
                                               dtype= torch.float32))

        # We can create parameters automaticely with torch.nn.Linear()
        self.linear_layer = torch.nn.Linear(in_features=  1,       # size of each input sample.
                                            out_features= 1)       # size of each output sample.


    # We have to over-write this method in our model because we inherit from nn.Module
    def forward(self, x: torch.Tensor) -> torch.Tensor:              # x is our input.
        return self.weight * x + self.bias                           # This is Linear Regression Formula, We want to correct thos attributes (self.weight, self.bias)
        # self.linear_layer(x)

# Set a manual seed.
torch.manual_seed(42)

# Create our instance from our class.
model0 = LRM()

# Get our Parameters in the instance.
list(model0.parameters())     # Return a list contains out parameters.
model0.state_dict()           # Return a named parameters.


# Loss Function Optimizer---------------------------------------------------------

# **Loss Function** : A function to measure how wrong our model's predictions (outputs) are to the ideal (acual values) outputs, lower is better.
# **Optimizer**     : Takes into account the loss of a model and adjusts the model's parameters (e.g. weight & bias in our case) to improve the loss function.


# Choose our (loss function).
# We will use L1loss but there are several loss functions in pytorch - https://pytorch.org/docs/stable/nn.html#loss-functions
loss_fn = torch.nn.L1Loss()     # L1 also called (MAE) stands for Maen Absolut Error.


# choose our (optimizers).
# Also There is many opimizers in pytorch in the module torch.optim - https://pytorch.org/docs/stable/optim.html
# We will use now SGD algorithm.
# We have to set a leaning rate(lr) that is the most important hyperparameter in machine laerning.
# Learning rate defines how sensetive the optimizer in to the change of loss function.
lr = 0.01           # Let's set learning rate to 0.01 from experience.  
optim = torch.optim.SGD(params= model0.parameters(),
                        lr= lr)

# Training & Testing loops---------------------------------------------------------


# Set the looping times.
epochs = 500

# Loop though data and do some steps...
for epoch in range(epochs):



### Training

    # Set to Training mode.
    model0.train()                         # Train sets all parameters that requires gradients to requires gradients

    # 1. Forward pass.
    y_pred = model0(xtrain)

    # 2. Calculate the loss
    loss = loss_fn(y_pred, ytrain)

    # 3. Set Optimizer to zero.
    optim.zero_grad()                     # To itilize performing gradient descent.

    # 4. Perform backpropagation on the loss with respect of model parameters.
    loss.backward()

    # 5. Step optimizer (perform gradient descent)
    optim.step()                          # By default optimizer will accumulate though the loop.

    # Training loop finished. just 5 steps.



    ### Testing 

    # Set to testing (evaluating) mode.
    model0.eval()                  # Thes line of code removes all extra claculation that not needed in testing.

    with torch.inference_mode():  # This line turn gradient tracking & couple more -not needed- things.
        # 1. Forward pass
        testpred = model0(xtest)

        # 2. Calculate the loss
        test_loss = loss_fn(testpred, ytest)

        # 3. print out what happen.
        if epoch % 100 == 0:
            print(f"Epoch: {epoch} || loss: {loss} || Test loss: {test_loss}")


# Saving & Loading a model-----------------------------------------------------------


#|> there are Three methods the save or load our model:
#  * torch.save()
#  * Save entire model
#  * torch.lead()
#  * torch.nn.Module.lead_state_dict()

# Import path library that come with pytorch
from pathlib import Path


### Save  the model.
# 1. Create a models directory
model_dir = Path('Results/models')
model_dir.mkdir(parents= True, exist_ok= True)

# 2. Create a models file path.
model_name = "model1.pth"
save_path  = model_dir / model_name

# 3. Save the model.
torch.save(model0.state_dict(), save_path)


### Load the model.
# 1. Create an instace from our model class
loaded_mdl0 = LRM()

# 2. Use torch.nn.Module.lead_state_dict()
loaded_mdl0.load_state_dict(torch.load(save_path, weights_only= True))



# =================================================================================================
#### CLASSIFICATIONS===============================================================================
# =================================================================================================

#|> We will learn about differernt types of neural networks in this section.
#|> Each problem has is unique solution and neural structure.


# Create a new model (circles)-------------------------------------------------------

#|> We will build a neural network for binary classification.
#|> We will import  our data from scikit learn.
#|> the data is actually two circles in 2D space.
#|> The data are labeled (1 or 0) for each circle.
#|> In this model we will use two linear layers.
#|> Model contains 1 hidden layer which has 5 neurons.
#|> This is our first multi-layer neural network.

# os.system('cls') # For consontration perposes.

# Import the data.
from sklearn.datasets import make_circles
import numpy as np

n_samples = 1000
X, y = make_circles(n_samples,
                    noise= 0.02,
                    random_state= 42)  # Same to menual seed in pytorch.

# Trun it to tensors
X = torch.from_numpy(X).float()
y = torch.from_numpy(y).float().unsqueeze(1)

# Split the data.
split = int(0.8*(len(X)))
X_train, X_test = X[: split], X[split: ]
y_train, y_test = y[: split], y[split: ]

# Create a subclass from torch.nn.Module
class circle0(torch.nn.Module):
    # Constractor
    def __init__(self) -> None:
        super().__init__()
        # Define our layers.
        self.linear1 = torch.nn.Linear(in_features= 2, out_features= 5) # We choose in features in same size of X[0] which is 2
        self.linear2 = torch.nn.Linear(in_features= 5, out_features= 1) # We choose out features in same size of y[0] which is 1 (or scaler)

    def forward(self, x):                     # Implement the neural network calculations in forward pass (forward method)
        return self.linear2(self.linear1(x))  # x -> linear1 -> linear2
    
# agnistic device.
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# Create an instance from the class.
model1 = circle0().to(device)


# There are other ways to writ less code but it will perform same code above.
class circle1(torch.nn.Module):
    def __init__(self) -> None:
        super().__init__()
        # Define our layers with Sequential.
        self.layers = torch.nn.Sequential(
                          torch.nn.Linear(in_features= 2, out_features= 5),
                          torch.nn.Linear(in_features= 5, out_features= 1))


    def forward(self, x):
        return self.layers(x)  # We dont need to write our layers manualy 

# Create the class instance.
model2 = circle0().to(device)

# There are more easier way.
model3 = torch.nn.Sequential(
    torch.nn.Linear(in_features= 2, out_features= 5),
    torch.nn.ReLU(),
    torch.nn.Linear(in_features= 5, out_features= 1))


#|> torch.nn.BCELoss()             | Creates a loss function that measures the binary cross entropy between the target (label) and input (features).
#|> torch.nn.BCEWithLogitsLoss()   | This is the same as above except it has a sigmoid layer (nn.Sigmoid) and it's more stable.


# Choose our loss function and the optimizer.
loss_fn = torch.nn.BCEWithLogitsLoss() # binary cross entropy

# Choose optimizer.
optimizer = torch.optim.SGD(model3.parameters(), lr= 0.1)   # Stands for Stacestic gradient decent.

def accuracy(y_true, y_pred):
    correct = torch.eq(y_true, y_pred).sum().item()  # torch.eq() calculates where two tensors are equal
    return (correct / len(y_pred))*100


# Row logits --> probabilities --> binary labels

model3(X_test.to(device))[:5]

# Use torch.softmax if you work with multiclass classifications.
# Turn our neural network logits (Outputs) to probabilities by sigmoid activation function.
y_pred_probs = torch.sigmoid(model3(X_test.to(device))[:5])  # To probabilities

# Covert it to binary labels.
y_lbls = torch.round(y_pred_probs)  # To binary labels


# training 

# Set manual seed
torch.manual_seed(42)
torch.cuda.manual_seed(42)

# transform our data to device.
X_train, y_train = X_train.to(device), y_train.to(device)
X_test, y_test  = X_test.to(device), y_test.to(device)

# Epochs hyperparameter.
epochs = 1000

for epoch in range(epochs):

    model3.train()

    # forward pass
    y_pred = model3(X_train)

    loss = loss_fn(y_pred, y_train)
    optimizer.zero_grad()

    loss.backward()
    optimizer.step()


    # Testing
    if epoch % 1000 == 0:
        model3.eval()
        with torch.inference_mode():
            y_test_preds = model3(X_test)
            y_tst_lbls = torch.round(torch.relu(y_test_preds))

            tstloss = loss_fn(y_tst_lbls, y_test)

        print(f"Test Loss: {tstloss}")



# =================================================================================================
#### COMPUTER VISION===============================================================================
# =================================================================================================


# We will use TorchVision for computer vision problems.
import torchvision
from torchvision import datasets
from torchvision import transforms
from torchvision.transforms import ToTensor

import matplotlib.pyplot as plt


# 1. Getting a dataset 
# For this example we will use fasion MNIST dataset from torchvision.datasets .
train_data = datasets.FashionMNIST(
    root= 'dataset',                                       # Whare to download data
    train= True,                                           # Is training data or testing data.
    download= True,                                        # Do we want to download the data.
    transform= ToTensor(),                                 # Do We want to tramsform data.
    target_transform= None                                 # Do We want to tramsform labels.
)

test_data = datasets.FashionMNIST(
    root= 'dataset',                                       # Whare to download data
    train= True,                                           # Is training data or testing data.
    download= True,                                        # Do we want to download the data.
    transform= ToTensor(),                                 # Do We want to tramsform data.
    target_transform= None                                 # Do We want to tramsform labels.
)

image, label = train_data[0]                               # Return the image with it's label.

train_data.classes                                         # Return classes of our data.
train_data.class_to_idx                                    # Return classes of our data with coresponding index.

train_data.data                                            # Return our data.
train_data.targets                                         # Return our labels.


cls =train_data.classes
image, label = train_data[0]
fig = plt.figure(figsize= (9, 9))
rows, cols = 4, 4
for i in range(1, rows*cols +1):
    Ridx = torch.randint(0, len(train_data), size= [1]).item()
    img, label = train_data[Ridx]
    fig.add_subplot(rows, cols, i)
    plt.imshow(img.squeeze(), cmap="gray")
    plt.title(cls[label])
    plt.axis(False)
plt.show()
