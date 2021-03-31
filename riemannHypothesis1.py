# This program will not necessarily use sympy but aims to build on
# testing the conjecture on Riemann hypothesis ...
from math import *
from matplotlib import pyplot as plt
from random import random
def riemannSum(s): # s can be complex number
    sum1, n = 0, 1
    x, y = s.real, s.imag
    maxTerm = 50
    for n in range(1,maxTerm+1):
        p1 = n**(-x)*cos(y*log(n))
        p1 = p1  - (n**(-x)*sin(y*log(n)))*1j
        sum2 = sum1
        sum1 = sum1 + p1
        print(round(s,3),n,round(sum1,3),
        round(abs(sum2-sum1),3))
    return sum1
print(round(1.2341453,3))
# conjectureRiemann1 = lambda s,t: riemannSum(s+t*1j)
# N1 = 5000
# maxlim = 100
# r = maxlim*random()
# x = [0.1*k for k in range(N1)]
# y = [abs(conjectureRiemann1(r,0.1*k)) for k in range(N1)]
# plt.plot(x,y)
# plt.show()