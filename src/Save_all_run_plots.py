import numpy as np
import matplotlib.pyplot as plt
from functionClass import function as func

#prompt user for parameters

algorithms = ["DE","PSO"]
functions = [1,2,3,4,5,6,7,8,9]
Dimensions = [10,30,50]

for algo in algorithms:
    for fn in functions:
        for D in Dimensions:
            #setup filename
            fileName = str(D) + "_" + str(fn) + "_" + algo + ".csv"
            filePath = "../output/" + fileName
            data = np.genfromtxt(filePath,dtype=[('run','i8'),('NFC','i8'),('Fitness Error','f8')],comments='#',delimiter=','
                                 ,skip_footer=0,converters=None,missing_values=None,filling_values=None,usecols=([2]))

            functionList=func.get_functionsList()
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

            plt.title(functionList[fn-1] + "\n"+ algo + ", D = " + str(D) + ", Log Scale")
            plt.ylabel("Fitness Error")
            plt.xlabel("NFC")
            plt.yscale('symlog')
            plt.savefig("../img/all_runs/" +algo+"_"+str(fn)+"_"+str(D)+".png", bbox_inches='tight')
            plt.close()
            #plt.show()