#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 13:14:02 2021

@author: shrohanmohapatra
"""

from sympy import symbols, integrate, simplify
x, y = symbols('x y')
print(simplify(integrate(1/(1-x**2-y**2),(y,0,1-x))))

# Answer to the above
# sqrt(-1/(x**2 - 1))*(-log(sqrt(-1/(x**2 - 1))*(1 - x**2)) \
# + log(sqrt(-1/(x**2 - 1))*(x**2 - 1)) + \
# log(-x**2*sqrt(-1/(x**2 - 1)) - x + sqrt(-1/(x**2 - 1)) + 1) \
# - log(x**2*sqrt(-1/(x**2 - 1)) - x - sqrt(-1/(x**2 - 1)) + 1))/2

# Monte Carlo summation 

from random import random
from math import log, sqrt
G = 0
err = 10**(-5)
A = []
while True:
    x = random()
    print('x = ',x)
    term1 = -log(sqrt(-1/(x**2 - 1))*(1 - x**2))
    print('term1 = ',term1)
    term2 = log(sqrt(-x**2 + 1))
    print('term2 = ',term2)
    term3 = log(-x**2*sqrt(1/(-x**2 + 1)) - x + sqrt(1/(-x**2 + 1)) + 1)
    print('term3 = ',term3)
    term4 = -log(x**2*sqrt(1/(-x**2 + 1)) - x - sqrt(1/(-x**2 + 1)) + 1)
    print('term4 = ',term4)
    term = sqrt(1/(-x**2 + 1))*(term1+term2+term3+term4)/2
    print('term = ',term)
    print('Small checkpoint')
    if term in A: continue
    A.append(term)
    G1 = G
    G = G + term
    print(x,G)
    if abs(G-G1)/abs(G) < err: break
print(A, G, len(A))
# print('Calculated value of Catalan%s constant',G/len(A))