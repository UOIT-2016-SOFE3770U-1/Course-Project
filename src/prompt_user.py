from functionClass import function as func
import numpy as np

def algorithm():
    algorithm_choice = None
    while algorithm_choice not in {"de", "pso"}:
        algorithm_choice = input("Please choose algorithm type\n"
                                 "Write in small case 'de' for Differential evolution\n"
                                 "Write in small case 'pso' for Particle swarm optimization\n")
    return algorithm_choice


def function():
    functionList= func.get_functionsList()

    for i in functionList:
        print(i)

    function_choice = input("Choose a function from the list above.\n"
                            "Please enter a number form 1 to 9\n")
    print("You choose:\n", functionList[int(function_choice)-1])

    # Create function object from function class
    # Create function object here to pass it to algorithm and keep track of NFC

    return int(function_choice)


def dimensions():
    D = input("Enter space separated integers for dimensions\n"
              "Example:10 30 50\n")
    D = D.split()
    D = np.int_(D)
    return D


def runs():
    runFrom = int(input("From Run Number: "))
    runTo = int(input("To Run Number: "))
    return [runFrom,runTo]
