from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

def plot3D(fn, xLowerBound, xUpperbound, yLowerBound, yUpperbound,name):
    X = np.linspace(xLowerBound, xUpperbound, 200)  # points from 0..10 in the x axis
    Y = np.linspace(yLowerBound, yUpperbound, 200)  # points from 0..10 in the y axis
    X, Y = np.meshgrid(X, Y)  # create meshgrid
    Z = fn([X, Y])  # Calculate Z

    # Plot the 3D surface for function from project
    fig = plt.figure(name)
    ax = fig.gca(projection='3d')  # set the 3d axes
    ax.plot_surface(X, Y, Z,
                    rstride=3,
                    cstride=3,
                    alpha=0.3,
                    cmap='hot')
    plt.show()