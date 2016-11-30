from pathlib import Path
import datetime
from functionClass import function as func
from DeClass import DE
from psoClass import pso
import numpy as np
#import pso

#fnc = function()
Np = 100
Cr = 0.9
F = 0.8

# variables for PSO
C1 = 2.05
C2 = 2.05
inertiaWeightStartRange = 0.9
inertiaWeightEndRange = 0.4

time_stamp = '{:%Y_%m_%d_%H_%M_%S}'.format(datetime.datetime.now())
def save_to_file(dimention, fuctionNumber, Algorithm, run, NFC, best):
    filePath = "../output/" + str(dimention) + "_" + str(fuctionNumber) + "_" + str(Algorithm) + "_" + str(time_stamp) + ".csv"
    if not Path(filePath).is_file():
        file = open(filePath, 'w')
    else:
        file = open(filePath, 'a')
    file.write(str(run) + ',' + str(NFC) + ',' + str(best) + '\n')
    file.close()


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

    # Create function object from fuction class
    # Create fucntion object here to pass it to algorithm and keep track of NFC
    function = func(int(function_choice))

    D = input("Enter space separated integers for dimensions")
    D = D.split()

    runFrom = int(input("From Run Number:"))
    runTo = int(input("\nTo Run Number:"))
    #functionToCall = getattr(fnc,"f"+function_choice)
    #functionToCall = fnc.fn


    if algorithm_choice == "de":

        for d in D:
            print(str(d))
            for i in range(runFrom, runTo+1):
                # Create function object from fuction class
                # Create fucntion object here to pass it to algorithm and keep track of NFC
                function = func(int(function_choice))
                # Create de object for De class
                de = DE(Np,d,Cr,F,function)

                best = de.get_best()
                NFC = function.get_NFC()
                save_to_file(d,function_choice,'DE', i, NFC,best)
                print("run: " + str(i))
                #print("Best = " + str(best) + "\n")
                #print("NFC = " + str(NFC))

                while NFC < 5000*int(d):
                    best = de.generate_test()
                    NFC = function.get_NFC()
                    #print("Best = " + str(best) + "\n")
                    #print("NFC = " + str(NFC))
                    save_to_file(d, function_choice, 'DE', i, NFC, best)
    elif algorithm_choice == "pso":
        for d in D:
            print(str(d))
            for i in range(runFrom, runTo+1):
                # Create function object from fuction class
                # Create fucntion object here to pass it to algorithm and keep track of NFC
                function = func(int(function_choice))
                # Create pso object from pso class
                PSO = pso(Np,d,C1,C2,-100,100,
                          inertiaWeightStartRange,inertiaWeightEndRange,
                          function)

                best = PSO.get_bestFunctionValue()
                NFC = function.get_NFC()
                save_to_file(d, function_choice, 'PSO', i, NFC, best)
                print("run: " + str(i))

                while NFC < 5000 * int(d):
                    PSO.run()
                    best = PSO.get_bestFunctionValue()
                    NFC = function.get_NFC()
                    save_to_file(d, function_choice, 'PSO', i, NFC, best)