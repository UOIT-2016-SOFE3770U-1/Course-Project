import numpy as np

#f1 :   High Conditioned Elliptic Function
#f2 :   Bent cigar Function
#f3 :   Discus Function
#f4 :   Rosenbrock's Function
#f5 :   Ackley's Function
#f6 :   Weierstrass Function
#f7 :   Griewank's Function
#f8 :   Rastrigin's Function
#f9 :   Katsuura Function

#f1 :   High Conditioned Elliptic Function
def f1(x):
    sum = 0.0
    for i in range(1, len(x) + 1):
        sum += ((10**6) ** ((i - 1) / (len(x) - 1))) * (x[i - 1] ** 2)
    return sum


#f2 :   Bent cigar Function
def f2(x):
    sum = 0.0
    for i in range(2, len(x) + 1):
        sum += x[i - 1] ** 2
    sum *= 10**6
    sum += x[0] ** 2
    return sum

#f3 :   Discus Function
def f3(x):
    sum1,sum2 = 0.0 , 0.0

    sum1 = x[1] ** 2
    sum1 *= 10**6
    for i in range (2, len(x)+1):
        sum2 += x[i - 1] ** 2

    result = sum1 + sum2
    return result

#f4 :   Rosenbrock's Function
def f4(x):
    sum = 0.0
    for i in range(1, len(x)):
        sum += (100 * (((x[i - 1] ** 2) - x[i])**2)) + ((x[i - 1] - 1) ** 2)
        return sum


#f5 :   Ackley's Function
def f5(x):
    sum1, sum2 = 0.0, 0.0
    for i in range(1, len(x)):
        sum1 += x[i-1] ** 2
    sum1 = sum1 / float(len(x))
    sum1 **= 0.5
    for i in range(1, len(x)):
        sum2 += np.cos(2 * np.pi * x[i-1])
    sum2 = sum2 / float(len(x))

    exp1 = -20.0 * (np.e ** (-0.2 * sum1))
    exp2 = np.e ** sum2

    result = exp1 - exp2 + 20 + np.e
    return result


#f6 :   Weierstrass Function
#f7 :   Griewank's Function
#f8 :   Rastrigin's Function
def f8(x):
    sum = 0.0
    for i in range(1, len(x)):
        sum += (x[i-1] ** 2 - 10 * np.cos(2 * np.pi * x[i-1]) + 10)
    return sum

#f9 :   Katsuura Function
