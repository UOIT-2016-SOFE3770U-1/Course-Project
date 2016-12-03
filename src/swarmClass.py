import numpy as np
from particleClass import Particle as Prt


class swarm:
    """swarm class for PSO algorithm"""
    __dimension = None
    __function = None
    __variableLowerBound = None
    __variableUpperBound = None
    __inertiaWeight = None
    __C1 = None
    __C2 = None
    __Np = None
    __bestPosition = None
    __bestFunctionValue = None
    __particles = None
    __NFC = 0

    def __init__(self, Np,
                 dimension,
                 function,
                 VariableLowerBound,
                 VariableUpperBound,
                 C1, C2,
                 inertiaWeightStartRange,
                 inertiaWeightEndRange):
        self.__Np = Np
        self.__dimension = dimension
        self.__function = function
        self.__variableLowerBound = VariableLowerBound
        self.__variableUpperBound = VariableUpperBound
        self.__C1 = C1
        self.__C2 = C2
        self.__inertiaWeight = np.linspace(inertiaWeightStartRange, inertiaWeightEndRange, Np)
        self.__particles = np.empty(Np, dtype=Prt)
        i = 0
        # generate unique particles in the swarm
        while i < Np:
            self.__particles[i] = self.create_particle()
            #print("created particel ", i)
            j=0
            for j in range (0, i):
                if np.array_equal(self.__particles[i],self.__particles[j]):
                    i = i - 1
                    break
            if self.__bestFunctionValue == None:
                self.__bestFunctionValue = self.__particles[i].get_bestFunctionValue()
                self.__bestPosition = self.__particles[i].get_bestPosition()
                bestNFC = self.__function.get_NFC()
            if self.__bestFunctionValue > self.__particles[i].get_bestFunctionValue():
                self.__bestFunctionValue = self.__particles[i].get_bestFunctionValue()
                self.__bestPosition = self.__particles[i].get_bestPosition()
            i = i + 1


    def get_bestPosition(self):
        return self.__bestPosition

    def get_bestFunctionValue(self):
        return self.__bestFunctionValue

    def create_particle(self):
        particle = Prt(self.__dimension,
                       self.__function,
                       self.__variableLowerBound,
                       self.__variableUpperBound)
        return particle

    def update_particle(self, index):
        # update velocity
        self.__particles[index].update_velocity(self.__inertiaWeight[index], self.__C1,self.__C2,self.__bestPosition)
        # Move to new position and
        self.__particles[index].update_position()
        # check and update if new particle's postion is better than the global' position
        if self.__bestFunctionValue > self.__particles[index].get_bestFunctionValue():
            self.__bestFunctionValue = self.__particles[index].get_bestFunctionValue()
            self.__bestPosition = self.__particles[index].get_bestPosition()

    def run(self):
        for i in range(0, self.__Np):
            # Update velocities and move to new poition
            self.update_particle(i)
            self.__bestFunctionValue = self.get_bestFunctionValue()
            self.__bestPosition = self.get_bestPosition()
