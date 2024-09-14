import matplotlib.pyplot as plt
import torch
from os import system
system('cls')

W = 80
b = 0.5


x = torch.arange(0, 1, 0.02).unsqueeze(dim=1)
y = W * x + b


split_border = int(0.8 * len(x))

xtrain, ytrain = x[:split_border], y[:split_border]
xtest, ytest   = x[split_border:], y[split_border:] 


def plot(X1, Y1, X2, Y2):
    plt.scatter(X1, Y1, c= "r", s= 4, )
    plt.scatter(X2, Y2, c= "g", s= 4, )
    plt.title("LRM")
    plt.grid(True)
    plt.show()

class LRM(torch.nn.Module):

    def __init__(self):
        super().__init__()

        self.weight = torch.nn.Parameter(torch.randn(1))
        self.bias   = torch.nn.Parameter(torch.randn(1))

    def forward(self, x):
        return self.weight*x + self.bias
    

torch.manual_seed(42)         # To make random numbers same.
mdl_0 = LRM()

with torch.inference_mode():  # To disable all unrequired calculations like: required_grad, Others
    ypred = mdl_0(xtest)

# plot(x, y, xtest, ypred)

loss_fn = torch.nn.L1Loss()
optim = torch.optim.SGD(mdl_0.parameters(), lr= float(input("lr    : "))) # 0.01 

epochs = int(input("epochs: "))  # 1000

for _ in range(epochs):

    mdl_0.train()
    ypred = mdl_0(xtrain)
    loss = loss_fn(ypred, ytrain)
    optim.zero_grad()
    loss.backward()
    optim.step()

print(f"loss  :", round(float(loss), 3))
print(f'score : {int((1/loss)*100)}')
print(f"Weight: {round(float(list(mdl_0.parameters())[0]), 3)} --> {W}")
print(f"Bias  : {round(float(list(mdl_0.parameters())[1]), 3)} --> {b}")
