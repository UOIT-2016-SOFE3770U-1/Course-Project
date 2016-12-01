import numpy as np
import matplotlib.pyplot as plt

#prompt user for parameters

algo = input("Enter ' DE ' for Differntional Evolution.\n Or,' PSO ' for Population Particle swarm optimization ")
fn = input("Enter function Number ")
D = input("Enter variable dimensions ")

#setup filename
fileName = D + "_" + fn + "_" + algo + ".csv"
filePath = "../output/" + fileName
data = np.genfromtxt(filePath,dtype=[('run','i8'),('NFC','i8'),('Fitness Error','f8')],comments='#',delimiter=','
                     ,skip_footer=0,converters=None,missing_values=None,filling_values=None,usecols=([2]))

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
if int(D)== 10:
    NFC = range(1,50000,100)
    for i in range(0,12500,500):
        plt.plot(NFC,data[i:i+500])



elif int(D)== 30:
    NFC = range(1,150000,100)
    for i in range(0,37500,1500):
        plt.plot(NFC,data[i:i+1500])

elif int(D)== 50:
    NFC = range(1,250000,100)
    for i in range(0,62500,2500):
        plt.plot(NFC,data[i:i+2500])


plt.title(functionList[int(fn)-1] + "\n"+ algo + ", D = " + D)
plt.yscale('log')
plt.show()