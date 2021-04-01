from sympy import *
from matplotlib import pyplot as plt
import numpy as np
from random import randint
y, n = symbols('y n')
f = cos(y*log(n+1))/cos(y*log(n))*(1+1/n)**(-1/2)
# print(limit(f,n,oo)) maximum recursion limit exceeded ....
print(
    cos(y*log(n+1))/cos(y*log(n)) == 
    cos(y*log(1+1/n))-tan(y*log(n))*sin(y*log(1+1/n))
)
Y = 13
M = 10000
n1 = np.linspace(2,M,M-1)
y1 = np.cos(Y*np.log(n1+1))/np.cos(Y*np.log(n1))*(1+1/n1)**(-1/2)
# y2 = (
#     np.cos(Y*np.log(1+1/n1))-np.tan(Y*np.log(n1))*np.sin(Y*np.log(1+1/n1))
# )*(1+1/n1)**(-1/2)
y2 = np.sin(Y*np.log(n1+1))/np.sin(Y*np.log(n1))*(1+1/n1)**(-1/2)
plt.plot(n1,y1)
plt.plot(n1,y2)
plt.show()
