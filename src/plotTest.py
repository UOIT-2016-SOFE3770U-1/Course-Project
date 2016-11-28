from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import functions as fn
from plot3D import plot3D

#f1 :   High Conditioned Elliptic Function
#f2 :   Bent cigar Function
#f3 :   Discus Function
#f4 :   Rosenbrock's Function
#f5 :   Ackley's Function
#f6 :   Weierstrass Function
#f7 :   Griewank's Function
#f8 :   Rastrigin's Function
#f9 :   Katsuura Function


plot3D(fn.f1,-5,5,-5,5,"1. High Conditioned Elliptic Function")
plot3D(fn.f2,-5,5,-5,5,"2. Bent cigar Function")
plot3D(fn.f3,-6,6,-6,6,"3. Discus Function")
plot3D(fn.f4,-5,5,-5,5,"4. Rosenbrock's Function")
plot3D(fn.f5,-5,5,-5,5,"5. Ackley's Function")
plot3D(fn.f6,-5,5,-5,5,"6. Weierstrass Function")
plot3D(fn.f7,-10,10,-10,10,"7. Griewank's Function")
plot3D(fn.f8,-5,5,-5,5,"8. Rastrigin's Function")
plot3D(fn.f9,0,0.25,0,0.25,"9. Katsuura Function")
