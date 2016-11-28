from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

def plot3D(fn):
    X = np.linspace(0, 100, 100)  # points from 0..10 in the x axis
    Y = np.linspace(0, 100, 100)  # points from 0..10 in the y axis
    X, Y = np.meshgrid(X, Y)  # create meshgrid
    Z = fn([X, Y])  # Calculate Z

    # Plot the 3D surface for function from project
    fig = plt.figure()
    ax = fig.gca(projection='3d')  # set the 3d axes
    ax.plot_surface(X, Y, Z,
                    rstride=3,
                    cstride=3,
                    alpha=0.3,
                    cmap='hot')
    plt.show()
