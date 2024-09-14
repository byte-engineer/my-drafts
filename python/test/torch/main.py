import torch
import torch.nn as nn
from torch.utils.data import DataLoader

import torchvision 
from torchvision import transforms
from torchvision.datasets import FashionMNIST

from func import accuracy_fn, imshow
import os
os.system('cls')


device = 'cuda' if torch.cuda.is_available() else 'cpu'



BATCHSIZE = 32
LR = 0.1
EPOCHS = 3


# Download our data.
train_data = FashionMNIST(
    root= 'data',
    train= True,
    download= True,
    transform=  transforms.ToTensor(),
    target_transform= None
)

test_data = FashionMNIST(
    root= 'data',
    train= False,
    download= True,
    transform=  transforms.ToTensor(),
    target_transform= None
)

# func.imshow(train_data)

# Load the data.
train_dataloader = DataLoader(dataset= train_data,
                              batch_size= BATCHSIZE,
                              shuffle= True)

test_dataloader = DataLoader(dataset= test_data,
                             batch_size= BATCHSIZE,
                             shuffle= True)


# Get all 10 classes
classes = train_data.classes

# imshow(train_data, 2, 2)
# exit()

class modelFashsion(nn.Module):

    def __init__(self, inputShape, hidden_units, outputShape):
        super().__init__()

        self.layers = nn.Sequential(
                      nn.Flatten(),
                      nn.Linear(inputShape, hidden_units),
                      nn.ReLU(),
                      nn.Linear(hidden_units, outputShape),
                      nn.ReLU()
        )

    def forward(self, X):
        return self.layers(X)


Model = modelFashsion(28*28, 60, len(classes)).to(device)


loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(params=Model.parameters(),
                            lr=LR)


for epoch in range(EPOCHS):

    print(f'Epoch: {epoch}')

    train_loss = 0

    for batch, (img,lbl) in enumerate(train_dataloader):
        
        Model.train()

        # 1. forward Pass.
        lbl_pred = Model(img)

        # 2. calculate the loss (per batch)
        loss = loss_fn(lbl_pred, lbl)

        # 3. Optimizer zero grade.
        optimizer.zero_grad()

        # 4. backward pass
        loss.backward()

        # 5. Step optimizer.
        optimizer.step()

        if batch % 400 == 0:
            # print(f"Looked at {batch * len(img)}/{len(train_dataloader.dataset)} samples.")

            print(float(loss))
    


    test_loss, test_acc = 0, 0
    Model.eval()
    with torch.inference_mode(): 
        for X_test, y_test in test_dataloader:
        # 1. Forward pass
            test_pred = Model(X_test)

        # 2. Calculate loss (accumulatively)
            test_loss += loss_fn(test_pred, y_test)

        # 3. Calculate accuracy
            test_acc += accuracy_fn(y_true=y_test, y_pred=test_pred.argmax(dim=1))

    # Calculate the test loss average per batch
    test_loss /= len(test_dataloader)

    # Calculate the test acc average per batch
    test_acc /= len(test_dataloader)

    # Print out what's happening
    print(f"\nTrain loss: {train_loss:.4f} | Test loss: {test_loss:.4f}, Test acc: {test_acc:.4f}")
