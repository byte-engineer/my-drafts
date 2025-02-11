# Draft/Librarys/Matplotlib.py

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as Axes3D
import numpy as np
import os
os.system('cls')

# Create a data.
X = np.linspace(0, 6.28, 50)
Y = np.sin(X)
Z = np.cos(X)


# 2D continus plotting.
def plot2D(X: np.ndarray,
           Y: np.ndarray,
           color= 'cyan',
           grid= True,
           xlbl= "X",
           ylbl= "Y",
           title= "Graph"):

    plt.plot(X, Y, color= color) 
    plt.title(title)                   # Set a title for the whole page.
    plt.xlabel(xlbl)                   # Label x axis with "X"
    plt.ylabel(ylbl)                   # Label y axis with "Y"
    plt.grid(grid)                     # Add grid to the graph.
    plt.show()                         # display the graph.


# 2D plotting by Dots.
def sctr(X: np.ndarray, Y: np.ndarray):
    # Variables
    length = len(X)
    area = np.random.rand(length) * 50
    colors = np.random.rand(length)

    # Actions
    plt.scatter(X, Y, s= area, c= colors, alpha= 0.5)  # the command that make the "dotty" graph.
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

# Same idea with no randoms.
def scatter_2D(X: np.ndarray,     # X data
            Y: np.ndarray,        # Y data
            color= None,          # Color of Dots, color deal with {hex, letters, rgb, rgba}.
            area= None,           # Size of dots.
            alpha= 1,             # Value from 0 to 1 for transperancy.
            xlbl= "X",            # Show the string in x axis.
            ylbl= "Y",            # Show the string in y axis.
            grid= False,          # Set or disable the grid.
            marker= "o",          # Marker {"o", "*", "+"}
            show= True
            ): 
    
    plt.scatter(X, Y, s= area, c= color, alpha= alpha, marker= marker)
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    plt.grid(grid)

    if show:
        plt.show()


def scatter_3D(X: np.ndarray,
               Y: np.ndarray,
               Z: np.ndarray,
               color= None,
               marker= 'o',         # Marker {'o', '*', '+'}
               xlbl= "X",
               ylbl= "Y",
               zlbl= "Z",
               projection= '3d',    # projection {'aitoff', 'hammer', 'lambert', 'mollweide', 'polar', 'rectilinear'}
               grid= True,
               show= True
               ):
    """
    Marker {'o', '*', '+'}\n
    projection {'aitoff', 'hammer', 'lambert', 'mollweide', 'polar', 'rectilinear'}
    """

    fig = plt.figure()
    ax = fig.add_subplot(111, projection= projection) # 111 --> Location in the window.
    ax.scatter(X, Y, Z, c= color, marker= marker)
    ax.grid(grid)
    
    # Set labels
    ax.set_xlabel(xlbl)
    ax.set_ylabel(ylbl)
    if projection == '3d':
        ax.set_zlabel(zlbl)
    
    if show:
        plt.show()


def plot_surface(X: np.ndarray,
               Y: np.ndarray,
               Z: np.ndarray,
               mode= 0,
               cmap= 'viridis',
               xlbl= "X",
               ylbl= "Y",
               zlbl= "Z",
               grid= True,
               show= True
               ):
    '''
    cmap => {'viridis', 'plasma', 'inferno', 'magma', 'cividis', 'coolwarm', 'rainbow', 'Greys'}
    '''    

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    if mode == 'wrfrm' or mode == 'wireframe' or mode == 1:
        ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
    else:
        ax.plot_surface(X, Y, Z, cmap= cmap)


    # Set labels
    ax.set_xlabel(xlbl)
    ax.set_ylabel(ylbl)
    ax.set_zlabel(zlbl)
    plt.grid(grid)
    if show:
        plt.show()


# fig = plt.figure(figsize= (9, 9))
# rows, cols = 4, 4
# for i in range(1, rows*cols +1):
#     Ridx = torch.randint(0, len(train_data), size= [1]).item()
#     img, label = train_data[Ridx]
#     fig.add_subplot(rows, cols, i)
#     plt.imshow(img.squeeze(), cmap="gray")
#     plt.title(cls[label])
#     plt.axis(False)
