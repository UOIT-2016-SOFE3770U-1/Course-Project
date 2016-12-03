from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from functionClass import function

#f1 :   High Conditioned Elliptic Function
#f2 :   Bent cigar Function
#f3 :   Discus Function
#f4 :   Rosenbrock's Function
#f5 :   Ackley's Function
#f6 :   Weierstrass Function
#f7 :   Griewank's Function
#f8 :   Rastrigin's Function
#f9 :   Katsuura Function

fnc = function()

#used codes from Tutorial
def plot3D(fn, xLowerBound, xUpperbound, yLowerBound, yUpperbound,name):
    X = np.linspace(xLowerBound, xUpperbound, 200)  # points in the x axis
    Y = np.linspace(yLowerBound, yUpperbound, 200)  # points in the y axis
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
    #plt.savefig("../img/2d3D/" + name + ".png", bbox_inches='tight')
    #plt.close()
    plt.show()

plot3D(fnc.f1,-5,5,-5,5,"1. High Conditioned Elliptic Function")
plot3D(fnc.f2,-5,5,-5,5,"2. Bent cigar Function")
plot3D(fnc.f3,-6,6,-6,6,"3. Discus Function")
plot3D(fnc.f4,-5,5,-5,5,"4. Rosenbrock's Function")
plot3D(fnc.f5,-5,5,-5,5,"5. Ackley's Function")
plot3D(fnc.f6,0,1,0,1,"6. Weierstrass Function")
plot3D(fnc.f7,-4,4,-4,4,"7. Griewank's Function")
plot3D(fnc.f8,-5,5,-5,5,"8. Rastrigin's Function")
plot3D(fnc.f9,0,0.5,0,0.5,"9. Katsuura Function")
