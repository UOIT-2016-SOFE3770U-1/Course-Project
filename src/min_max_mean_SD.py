import numpy as np
from pathlib import Path

runs = 25
Np = 100
#setup filename


for D in [10 , 30, #50
           ]:
    file_save = "../output/" + str(D) + "_" + "mean_worst_best_SD" + ".csv"
    file = open(file_save, 'w')
    file.write("DE_mean,PSO_mean,DE_worst,PSO_worst,DE_best,PSO_best,DE_SD,PSO_SD\n")
    file.close()
    for fn in [1, 2, 3, 4, 5, 6, 7, 8, 9]: # used this style instead of range
                                            #  to have more control of which function to include
        result = np.empty(8)
        for algo in ["DE", "PSO"]:
            fileName = str(D) + "_" + str(fn) + "_" + algo + ".csv"
            filePath = "../output/" + fileName

            data = np.genfromtxt(filePath,dtype=float,comments='#',delimiter=','
                                 ,skip_footer=0,converters=None,missing_values=None,filling_values=None,usecols=([2]))

            sum = np.sum(data)
            max = np.amax(data)
            min = np.amin(data)
            mean = np.mean(data)
            SD = np.std(data)

            if algo == "DE":

                result[0]= mean
                result[2] = max
                result[4] = min
                result[6] = SD
            elif algo == "PSO":
                result[1] = mean
                result[3] = max
                result[5] = min
                result[7] = SD

        file = open(file_save, 'a')
        for i in range(0,8):
            file.write(str(result[i]) + ',')
        file.write('\n')
        file.close()
