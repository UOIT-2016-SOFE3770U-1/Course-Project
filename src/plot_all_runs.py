import numpy as np
import matplotlib.pyplot as plt
import prompt_user
from functionClass import function as func

## Plot all runs for specific algorithm and function for choosen dimensions

#prompt user for parameters
algo = prompt_user.algorithm()
fn = prompt_user.function()
d = prompt_user.dimensions()

functionList=func.get_functionsList()

for D in d:
    # setup filename
    fileName = str(D) + "_" + str(fn) + "_" + algo + ".csv"
    filePath = "../output/" + fileName
    data = np.genfromtxt(filePath, dtype=[('run', 'i8'), ('NFC', 'i8'), ('Fitness Error', 'f8')], comments='#',
                         delimiter=','
                         , skip_footer=0, converters=None, missing_values=None, filling_values=None, usecols=([2]))

    if D == 10:
        NFC = range(1,50000,100)
        for i in range(0,12500,500):
            plt.plot(NFC,data[i:i+500])

    elif D == 30:
        NFC = range(1,150000,100)
        for i in range(0,37500,1500):
            plt.plot(NFC,data[i:i+1500])

    elif D == 50:
        NFC = range(1,250000,100)
        for i in range(0,62500,2500):
            plt.plot(NFC,data[i:i+2500])

    plt.title(functionList[int(fn)-1] + "\n"+ algo + ", D = " + str(D))
    plt.ylabel("Fitness Error")
    plt.xlabel("NFC")
    plt.yscale('symlog')
    #plt.savefig("../img/" +algo+"_"+fn+"_"+D+".png", bbox_inches='tight')
    plt.show()