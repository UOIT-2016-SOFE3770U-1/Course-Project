from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from plot3D import plot3D
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
'''
X = np.linspace(-5, 5, 200)
Y = np.linspace(-5, 5, 200)

fnc = function("../output/1.txt")
fnc.fn(1,X)'''

fnc = function()

plot3D(fnc.f1,-5,5,-5,5,"1. High Conditioned Elliptic Function")
plot3D(fnc.f2,-5,5,-5,5,"2. Bent cigar Function")
plot3D(fnc.f3,-6,6,-6,6,"3. Discus Function")
plot3D(fnc.f4,-5,5,-5,5,"4. Rosenbrock's Function")
plot3D(fnc.f5,-5,5,-5,5,"5. Ackley's Function")
plot3D(fnc.f6,-5,5,-5,5,"6. Weierstrass Function")
plot3D(fnc.f7,-10,10,-10,10,"7. Griewank's Function")
plot3D(fnc.f8,-5,5,-5,5,"8. Rastrigin's Function")
plot3D(fnc.f9,0,0.25,0,0.25,"9. Katsuura Function")
