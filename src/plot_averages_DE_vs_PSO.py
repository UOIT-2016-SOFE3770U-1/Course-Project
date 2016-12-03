import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import prompt_user
from functionClass import function as func
############################## important ###########################################
# to run this code you need two files for the same function with the same dimensions
# for example to plot the average for function 1, dimension 10:
# there should be in the folder '../output/' two files named:
# 10_1_DE.csv
# 10_1_PSO.csv
####################################################################################

functionList=func.get_functionsList()

#prompt user for parameters
#fn = prompt_user.function()
#d = prompt_user.dimensions()
d = [10, 30, 50]
#runs = 25
#setup filename

for fn in range(1,9+1):


    for D in d:

        fileName_DE = str(D) + "_" + str(fn) + "_" + "DE" + ".csv"
        fileName_pso = str(D) + "_" + str(fn) + "_" + "PSO" + ".csv"
        filePath_DE = "../output/" + fileName_DE
        filePath_pso = "../output/" + fileName_pso

        data_DE = np.genfromtxt(filePath_DE,dtype=float,comments='#',delimiter=','
                             ,skip_footer=0,converters=None,missing_values=None,filling_values=None,usecols=([2]))

        data_PSO = np.genfromtxt(filePath_pso,dtype=float,comments='#',delimiter=','
                             ,skip_footer=0,converters=None,missing_values=None,filling_values=None,usecols=([2]))

        sum_DE = np.zeros(50*D)
        sum_PSO = np.zeros(50*D)

        for i in range(0,50*D):
            for j in range(0+i,  (D*25*50)+i,50*D):
                sum_DE[i] += data_DE[j]
                sum_PSO[i] += data_PSO[j]

        average_DE = [x / (50*D) for x in sum_DE]
        average_PSO = [x / (50*D) for x in sum_PSO]

        NFC = range(1, (50*D*100), 100)
        plt.plot(NFC,average_DE,label="DE")
        plt.plot(NFC,average_PSO,label="PSO")
        plt.ylabel("Fitness Error")
        plt.xlabel("NFC")
        plt.yscale('symlog')
        plt.legend( loc=1,
                   ncol=2, mode="None", borderaxespad=0.)
        plt.title(functionList[int(fn)-1] + "\n"+ "DE vs. PSO" + ", D = " + str(D) + ", Log Scale")
        #plt.show()
        plt.savefig("../img/average_DE_vs_PSO/" + "DEvsPSO_D" + str(D) + "_fn" + str(fn) + "_" ".png", bbox_inches='tight')
        plt.close()

        # code to save the result to file
        '''
        file_save = "../output/" + str(D) + "_" + str(fn) + "_" + "compareAvrage" + "_" + ".csv"
        if not Path(file_save).is_file():
            file = open(file_save, 'w')
        else:
            file = open(file_save, 'w')

        for i in range(0, (50*D)):
            file.write(str(i*100) + ',' + str(average_DE[i]) + ',' + str(average_PSO[i]) + '\n')
        file.close()
        '''