from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import random
import matplotlib.pyplot as plt
import numpy as np
from functionClass import function as func
from pathlib import Path
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

class DE:

    __Np = 100
    __Cr = 0.9
    __F = 0.8
    __D = None  # Dimension
    __P = None # population
    __Pv = None
    __function = None
    __best = None
    #__NFC = None

    # D = 10, 30, 50
    #D = 10
    # Setup random population
    # Target Vector
    def __init__(self,Np, D, Cr, F, function):
        self.__Np = int(Np)
        self.__D = D
        self.__Cr = Cr
        self.__F = F
        self.__function = function
        # Create uniformly distributed random population
        self.__P = np.random.uniform(low=-100, high=100, size=(self.__Np, self.__D))
        # evaluate the population vectors
        self.__Pv=np.empty(self.__Np)
        for i in range(0,self.__Np):
            self.__Pv[i] = self.__function.fn(self.__P[i])
        # choose lowest value to be the best
        #self.__best = np.amin(self.__P)
        self.__best = self.__Pv[0]

    def get_best(self):
        return self.__best

    def generate_test(self):
        # X  Target Vector
        # Xv Traget Vector Value
        # Xa
        # Xb
        # Xc Third vector for mutation
        # V noisy vector
        # U

        for i in range(0, self.__Np):
            X = self.__P[i]
            Xv = self.__Pv[i]
            # select Xa, Xb, Xc
            y = np.random.choice(self.__Np, 3,replace=False)
            while i in y:
                y = np.random.choice(self.__Np, 3, replace=False)
            Xa = self.__P[y[0]]
            Xb = self.__P[y[1]]
            Xc = self.__P[y[2]]
            # Mutation
            # noisy vector
            V = (self.__F * (Xb - Xa)) + Xc
            ###########################################################
            # Crossover
            U = np.empty(self.__D)
            for j in range(0, self.__D):
                if np.random.random() < self.__Cr:
                    U[j] = V[j]
                else:
                    U[j] = X[j]
            ############################################################
            # U : Trial vector
            # Selection
            Uv = self.__function.fn(U)
            if (Uv <= Xv):
                X = U
                Xv = Uv
                self.__P[i] = X
                self.__Pv[i] = Xv
            if self.__best > Xv:
                self.__best = Xv
        return self.__best
