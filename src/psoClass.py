from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import random
import matplotlib.pyplot as plt
import numpy as np
from functionClass import function
from swarmClass import Swarm
from pathlib import Path
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


#variables
#NFC, MAX_NFC, NP, C1, C2, W, D
#Xi a particle
# fnV function value

Np = 100
C1 = 2.05
C2 = 2.05
# W = between 0.9 to 0.4 linearly decreasing
# D = 10, 30, 50
D =10
Max_NFC = 5000*D

class pso:
    __Np = None
    __C1 = None
    __C2 = None
    __W  = None
    __swarm = None
    __bestPosition = None
    __bestFunctionValue = None

    def __init__(self,Np, dimension, C1, C2,VariableLowerBound,VariableUpperBound,
                 inertiaWeightStartRange,inertiaWeightEndRange, function):
        self.__Np = int(Np)
        self.__D = int(dimension)
        self.__C1 = int(C1)
        self.__C2 = int(C2)
        #self.__W =
        self.__function = function
        # build the whole swarm
        # swarm size = NP
        self.__swarm = Swarm(self.__Np, self.__D, self.__function,
                      VariableLowerBound, VariableUpperBound, self.__C1, self.__C2,
                      inertiaWeightStartRange, inertiaWeightEndRange)
        self.__bestPosition = self.__swarm.get_bestPosition()
        self.__bestFunctionValue =self.__swarm.get_bestFunctionValue()


    def get_bestPosition(self):
        return self.__bestPosition

    def get_bestFunctionValue(self):
        return  self.__bestFunctionValue

# Range of variables [-100,100]
    def run(self):
        for i in range(0, Np):
            self.__swarm.update_particle(i)
            self.__bestFunctionValue = self.__swarm.get_bestFunctionValue()
            self.__bestPosition = self.__swarm.get_bestPosition()


    #print("best position is: ", swarm.get_bestPosition(), "\n")
    #print("best funcion value = ", swarm.get_bestFunctionValue())
