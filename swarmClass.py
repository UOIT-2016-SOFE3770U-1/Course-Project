import numpy as np
from particleClass import Particle as Prt


class Swarm:
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
            print("created particel ", i)
            for j in range (0, i):
                if np.array_equal(self.__particles[i],self.__particles[j]):
                    i = i - 1
                    break
            if self.__bestFunctionValue == None:
                self.__bestFunctionValue = self.__particles[i].get_bestFunctionValue()
                self.__bestPosition = self.__particles[i].get_bestPosition()
            if self.__bestFunctionValue > self.__particles[i].get_bestFunctionValue():
                self.__bestFunctionValue = self.__particles[i].get_bestFunctionValue()
                self.__bestPosition = self.__particles[i].get_bestPosition()
            i = i + 1
    def get_NFC(self):
        return self.__NFC

    def get_bestPosition(self):
        return self.__bestPosition

    def get_bestFunctionValue(self):
        return self.__bestFunctionValue

    def create_particle(self):
        particle = Prt(self.__dimension, self.__function,
                       self.__variableLowerBound,
                       self.__variableUpperBound)
        self.__NFC = self.__NFC + 1
        return particle

    def update_particle(self, index):
        # update velocity
        self.__particles[index].update_velocity(self.__inertiaWeight[index], self.__C1,self.__C2,self.__bestPosition)
        # Move to new position and
        self.__particles[index].update_position()
        # check if new postion is better
        if self.__bestFunctionValue > self.__particles[index].get_bestFunctionValue():
            self.__bestFunctionValue = self.__particles[index].get_bestFunctionValue()
            self.__bestPosition = self.__particles[index].get_bestPosition()
        self.__NFC = self.__NFC + 1
