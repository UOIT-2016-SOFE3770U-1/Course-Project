from pathlib import Path
from functionClass import function
import DE
import pso

fnc = function()

algorithm_choice = None
functionList=[
    "1.   High Conditioned Elliptic Function",
    "2.   Bent cigar Function",
    "3.   Discus Function",
    "4.   Rosenbrock's Function",
    "5.   Ackley's Function",
    "6.   Weierstrass Function",
    "7.   Griewank's Function",
    "8.   Rastrigin's Function",
    "9.   Katsuura Function"
]

sessionFile = Path("../output/session.txt")
if sessionFile.is_file() and input("previous session file found!\n"
                                   "Would you like to continue previous session? (y/n)") == "y":
        savedSession = open('../output/session.txt', 'r')
else:

    while algorithm_choice not in {"de", "pso"}:

        algorithm_choice = input("Please choose algorithm type\n"
            "Write in small case 'de' for Differential evolution\n"
            "Write in small case 'pso' for Particle swarm optimization\n")

    for i in functionList:
        print(
        i
        )

    function_choice = input("Choose a function from the list above.\n"
          "Please enter a number form 1 to 9\n")
    print("You choose:\n", functionList[int(function_choice)-1])

    D = input("Enter space separated integers for dimensions")
    D = D.split()

    runFrom = int(input("From Run Number:"))
    runTo = int(input("\nTo Run Number:"))
    #functionToCall = getattr(fnc,"f"+function_choice)
    #functionToCall = fnc.fn
    if algorithm_choice == "de":
        for d in D:
            for i in range(runFrom, runTo+1):
                DE.de(function_choice,i,int(d))
    elif algorithm_choice == "pso":
        for d in D:
            for i in range(runFrom, runTo+1):
                pso.pso(function_choice,i,int(d))
