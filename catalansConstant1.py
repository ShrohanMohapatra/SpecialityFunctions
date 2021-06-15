#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 12:25:01 2021

@author: shrohanmohapatra
"""

from sympy import symbols, integrate
from sympy.functions import atan
t = symbols('t')
print(integrate(1/t*atan(t),(t,0,1)))
# symbolic integration intractable
import math
print(math.atan(30)) # Seeing if math.atan works or not ...
# Using Monte Carlo summation ....
from random import random
G = 0
err = 10**(-3)
A = []
while True:
    t = random()
    term = atan(t)/t
    if term in A: continue
    A.append(term)
    G1 = G
    G = G + term
    print(G)
    if abs(G-G1)/G < err: break
print(A,len(A),G)
print('Calculated value of Catalan%s constant',G/len(A))