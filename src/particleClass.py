import random
import numpy as np


class Particle:
    """particle part of swarm for PSO algorithm"""
    __function = None
    __velocity = None
    __position = None
    __previousVelocity = None
    __previousPosition = None
    __bestPosition = None
    __functionValue = None
    __bestFunctionValue = None

    def __init__(self, dimension, function, VariableLowerBound, VariableUpperBound):
        self.__function = function
        self.__position = (VariableUpperBound - VariableLowerBound) * np.random.random_sample(dimension,) - VariableUpperBound
        self.__velocity = (VariableUpperBound - VariableLowerBound)/20 * np.random.random_sample(dimension,) - (VariableUpperBound/10)
        self.__bestPosition = self.__position
        self.__previousPosition = self.__position
        self.__previousVelocity = self.__velocity
        self.__functionValue = self.__function(self.__position)
        self.__bestFunctionValue = self.__functionValue


    def get_velocity(self):
        return self.__velocity

    def get_position(self):
        return self.__position

    def get_bestPosition(self):
        return self.__bestPosition

    def get_functionValue(self):
        return self.__functionValue

    def get_bestFunctionValue(self):
        return self.__bestFunctionValue

    def update_velocity(self,inertiaWeight, C1, C2, swarmBestPosition):
        p1 = random.random()
        p2 = random.random()
        #p1 = np.random.rand(0,1)
        #p2 = np.random.rand(0,1)
        self.__velocity = (inertiaWeight * self.__previousVelocity) + \
                          (p1 * C1) * (self.__bestPosition - self.__previousPosition) + \
                          (p2 * C2) * (swarmBestPosition - self.__previousPosition)

    def update_position(self):
        self.__position = self.__previousPosition + self.__velocity
        self.__functionValue = self.__function(self.__position)
        print("function value " , self.__functionValue, "\n")
        if (self.__functionValue < self.__bestFunctionValue):
            # update best function value
            self.__bestFunctionValue = self.__functionValue
            # update particle best position
            self.__bestPosition = self.__position
        return self.__bestPosition
