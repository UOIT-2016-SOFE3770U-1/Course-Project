from pathlib import Path
import datetime
import prompt_user
from functionClass import function as func
from DeClass import DE
from swarmClass import swarm

Np = 100

# variables for DE
Cr = 0.9
F = 0.8

# variables for PSO
C1 = 2.05
C2 = 2.05
inertiaWeightStartRange = 0.9
inertiaWeightEndRange = 0.4

time_stamp = '{:%Y_%m_%d_%H_%M_%S}'.format(datetime.datetime.now())


def save_to_file(dimension, fuctionNumber, algorithm, run, NFC, best):
    filePath = "../output/" + str(dimension) + "_" + str(fuctionNumber) + "_" + str(algorithm) + "_" + str(time_stamp) + ".csv"
    if not Path(filePath).is_file():
        file = open(filePath, 'w')
    else:
        file = open(filePath, 'a')
    file.write(str(run) + ',' + str(NFC) + ',' + str(best) + '\n')
    file.close()

algorithm_choice = prompt_user.algorithm()
function_choice = prompt_user.function()
D = prompt_user.dimensions()
runs = prompt_user.runs()
runFrom = runs[0]
runTo = runs[1]

if algorithm_choice == "de":

    for d in D:

        print(str(d))
        for i in range(runFrom, runTo+1):
            # Create function object from fuction class
            # Create function object here to pass it to algorithm and keep track of NFC
            function = func(int(function_choice))
            # Create de object for De class
            de = DE(Np,d,Cr,F,function)

            best = de.get_best()
            NFC = function.get_NFC()
            save_to_file(str(d),function_choice,'DE', i, NFC,best)
            print("run: " + str(i))
            #print("Best = " + str(best) + "\n")
            #print("NFC = " + str(NFC))

            while NFC < (5000 * d):
                best = de.generate_test()
                NFC = function.get_NFC()
                #print("Best = " + str(best) + "\n")
                #print("NFC = " + str(NFC))
                save_to_file(str(d), function_choice, 'DE', i, NFC, best)
elif algorithm_choice == "pso":
    for d in D:
        d = int(d)
        print(str(d))
        for i in range(runFrom, runTo+1):
            # Create function object from function class
            # Create function object here to pass it to algorithm and keep track of NFC
            function = func(int(function_choice))
            # Create pso object from swarm class
            PSO = swarm(Np,d,function,-100,100,C1,C2,
                        inertiaWeightStartRange,inertiaWeightEndRange)

            best = PSO.get_bestFunctionValue()
            NFC = function.get_NFC()
            save_to_file(str(d), function_choice, 'PSO', i, NFC, best)
            print("run: " + str(i))

            while NFC < (5000 * d):
                PSO.run()
                best = PSO.get_bestFunctionValue()
                NFC = function.get_NFC()
                save_to_file(str(d), function_choice, 'PSO', i, NFC, best)
