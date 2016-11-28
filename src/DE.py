from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import random
import matplotlib.pyplot as plt
import numpy as np
import functions as fn
from plot3D import plot3D

#variables
#NFC, MAX_NFC, NP, Xa, Xb, Xc, CR, F, D,

#f1 :   High Conditioned Elliptic Function
#f2 :   Bent cigar Function
#f3 :   Discus Function
#f4 :   Rosenbrock's Function
#f5 :   Ackley's Function
#f6 :   Weierstrass Function
#f7 :   Griewank's Function
#f8 :   Rastrigin's Function
#f9 :   Katsuura Function

NP = 100
Cr = 0.9
F = 0.8
# D = 10, 30, 50
D = 10
#fn = [fn.f1,fn.f2,fn.f3,fn.f4,fn.f5,fn.f6,fn.f7,fn.f8]
# Setup random population
# Target Vector
X = 200 * np.random.random_sample(D,) - 100
Xv = fn.f1(X)
for i in range(0,NP):
    # Two Random vectors
    Xa = 200 * np.random.random_sample(D,) - 100
    Xb = 200 * np.random.random_sample(D,) - 100
    # Third Random vector for mutation
    Xc = 200 * np.random.random_sample(D,) - 100
    while np.array_equal(X,Xa):
        Xa = 200 * np.random.random_sample(D,) - 100
    while np.array_equal(Xb, X) or np.array_equal(Xb, Xa):
        Xb = 200 * np.random.random_sample(D,) - 100
    while np.array_equal(Xc,X) or np.array_equal(Xc,Xa) \
            or np.array_equal(Xc,Xb):
        Xc = 200 * np.random.random_sample(D,) - 100
    ###################################################
    # Mutation
    #noisy vector
    V = (F * (Xb - Xa)) + Xc
    ###################################################
    # Crossover
    U = np.empty(D,)
    for i in range(0,D):
        x=np.random.random()
        if (x < Cr):
            U[i]=V[i]
        else:
            U[i]=X[i]
    ####################################################
    # Selection
    Uv = fn.f1(U)
    if (Uv<Xv):
        X = U
        Xv = Uv
    print(Xv)
print("Best Variable Vector:\n", X)
print("Best Solution: ", Xv)