import matplotlib.pyplot as plt
import numpy as np
import math
import random
import torchvision
import torch.utils
import torch.utils.data


def imshow(data: object, rows= 4, cols=4):

    # convert to numpy.

    # data = np.ndarray(data)

    # Estimate figsize
    figsize = ((math.isqrt(cols)+1)**2, (math.isqrt(rows)+1)**2)
    
    fig = plt.figure(figsize= figsize)

    # Classes & labels
    cls = data.classes


    for i in range(1, rows*cols+1):
        random_idx = torch.randint(0, len(data), size=[1]).item()
        img, label = data[random_idx]
        fig.add_subplot(rows, cols, i)
        plt.imshow(img.squeeze(), cmap="gray")
        plt.title(cls[label])
        plt.axis(False)
    plt.show()


def accuracy_fn(y_pred, y_true):

    correct = torch.eq(y_true, y_pred).sum().item()
    acc = (correct / len(y_pred)) * 100
    return acc
