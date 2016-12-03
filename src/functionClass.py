import numpy as np
from numba import jit

#f1 :   High Conditioned Elliptic Function
#f2 :   Bent cigar Function
#f3 :   Discus Function
#f4 :   Rosenbrock's Function
#f5 :   Ackley's Function
#f6 :   Weierstrass Function
#f7 :   Griewank's Function
#f8 :   Rastrigin's Function
#f9 :   Katsuura Function

class function:
    """"""
    __NFC = None
    __functionNumber = None

    def __init__(self,functionNumber=None):
        self.__NFC = 0
        self.__functionNumber = functionNumber

    def fn(self,x):
        """function call with one variable"""
        function_to_call = getattr(self, "f"+str(self.__functionNumber))
        result = function_to_call(x)
        self.__NFC += 1
        return result

    def get_NFC(self):
        return self.__NFC

    def get_functionNumber(self):
        return self.__functionNumber

    @staticmethod
    def get_functionsList():
        return [
                        "1.   High Conditioned Elliptic Function",
                        "2.   Bent cigar Function",
                        "3.   Discus Function",
                        "4.   Rosenbrock's Function",
                        "5.   Ackley's Function",
                        "6.   Weierstrass Function",
                        "7.   Griewank's Function",
                        "8.   Rastrigin's Function",
                        "9.   Katsuura Function"]

    #f1 :   High Conditioned Elliptic Function
    #@jit(nopython=True)
    def f1(self,x):
        sum = 0.0
        for i in range(1, len(x) + 1):
            sum += ((10**6) ** ((i - 1) / (len(x) - 1))) * (x[i - 1] ** 2)
        return sum


    #f2 :   Bent cigar Function
    #@jit(nopython=True)
    def f2(self,x):
        sum = 0.0
        for i in range(2, len(x) + 1):
            sum += x[i - 1] ** 2
        sum *= 10**6
        sum += x[0] ** 2
        return sum

    #f3 :   Discus Function
    #@jit(nopython=True)
    def f3(self,x):
        sum1,sum2 = 0.0 , 0.0

        sum1 = x[0] ** 2
        sum1 *= 10**6
        for i in range (2, len(x)+1):
            sum2 += x[i - 1] ** 2

        result = sum1 + sum2
        return result

    #f4 :   Rosenbrock's Function
    #@jit(nopython=True)
    def f4(self,x):
        sum = 0.0
        for i in range(1, len(x)+1-1):
            sum += (100 * (((x[i - 1] ** 2) - x[i])**2)) + ((x[i - 1] - 1) ** 2)
            return sum


    #f5 :   Ackley's Function
    #@jit(nopython=True)
    def f5(self,x):
        sum1, sum2 = 0.0, 0.0
        for i in range(1, len(x)+1):
            sum1 += x[i-1] ** 2
        for i in range(1, len(x)):
            sum2 += np.cos(2 * np.pi * x[i-1])

        exp1 = np.exp(-0.2 * np.sqrt((1/len(x))*sum1))
        exp2 = np.exp((1/len(x))*sum2)

        result = -20 * exp1 - exp2 + 20 + np.e
        return result


    #f6 :   Weierstrass Function
    #@jit(nopython=True)
    def f6(self,x):
        sum1,sum2,sum3 =0,0,0
        a=0.5
        b=3
        kmax=20
        for i in range(1, len(x)+1):
            for k in range(0,kmax+1):
                sum2 += a**k * np.cos(2 * np.pi * b**k * (x[i-1] + 0.5))
            sum1 += sum2
        for k in range(0,kmax+1):
            sum3 += a**k * np.cos(2 * np.pi * b**k * 0.5)
        result = sum1 - (len(x) * sum3)
        return  result

    #f7 :   Griewank's Function
    #@jit(nopython=True)
    def f7(self,x):
        sum,product = 0,1
        for i in range(1,len(x)+1):
            sum += (x[i-1]**2)/4000
        for i in range(1,len(x)+1):
            product *= np.cos(x[i-1]/np.sqrt(i))+1
        result = sum - product
        return result

    #f8 :   Rastrigin's Function
    #@jit(nopython=True)
    def f8(self,x):
        sum = 0.0
        for i in range(1, len(x)+1):
            sum += (x[i-1] ** 2 - 10 * np.cos(2 * np.pi * x[i-1]) + 10)
        return sum

    #f9 :   Katsuura Function
    #@jit(nopython=True)
    def f9(self,x):
        sum, product = 0,1
        for i in range(1,len(x)+1):
            for j in range(1, 32+1):
                sum += (np.absolute((2**j * x[i-1]) - (np.round(2**j * x[i-1])))/2**j)
            product *= np.power((1 + i * sum),(10/(len(x)**1.2)))
        result = (10/(len(x)**2)) * product - 10/(len(x)**2)
        return  result
