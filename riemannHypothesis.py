# This program will not necessarily use sympy but aims to build on
# testing the conjecture on Riemann hypothesis ...
from math import *
from matplotlib import pyplot as plt
def riemannSum(s): # s can be complex number
    sum1, sum2, n = 0, 1, 1
    precision = 10**(-2)
    x, y = s.real, s.imag
    while abs(sum2-sum1)>=precision:
        print(s,n,abs(sum2-sum1))
        sum1 = sum2
        p1 = n**(-x)*cos(y*log(n))
        p1 = p1  - (n**(-x)*sin(y*log(n)))*1j
        sum2 = sum1 + p1
        n = n + 1
    return sum2
conjectureRiemann = lambda t: riemannSum(0.5+t*1j)
N1 = 1000
x = [k for k in range(N1)]
y = [conjectureRiemann(k) for k in range(N1)]
plt.plot(x,y)
plt.show()