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



# Range of variables [-100,100]

def pso(functionNumber,run,D):
    filePath = "../output/" + str(D) + "_" + str(functionNumber) + "_" + str(run) + "_PSO.csv"
    if not Path(filePath).is_file():
        file = open(filePath, 'w')
        file.close()
    fnc = function(filePath,functionNumber,run)
    NFC = 0
    # build the whole swarm
    # swarm size = NP
    swarm = Swarm(Np,D, fnc, -100, 100, C1, C2, 0.9, 0.4)

    while NFC < Max_NFC:
        for Xi in range(0, Np):
            swarm.update_particle(Xi)
            bestValue = swarm.get_bestFunctionValue()
            bestPosition = swarm.get_bestPosition()
            bestNFC = fnc.get_NFC()
            file = open(filePath, 'a')
            file.write(str(bestNFC) + ',' + str(bestValue) + ',')
            for i in bestPosition:
                file.write(str(i) + ',')
            file.write("\n")
            file.close()
        NFC = fnc.get_NFC()

    print("best position is: ", swarm.get_bestPosition(), "\n")
    print("best funcion value = ", swarm.get_bestFunctionValue())
