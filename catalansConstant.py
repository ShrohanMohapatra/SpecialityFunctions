#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 11:27:02 2021

@author: shrohanmohapatra
"""

from sympy import Symbol, residue, E, I, pi
z = Symbol('z')
print(residue(E**(I*pi*z)/(2*z+1)**2,z,-1/2))
from sympy import symbols, integrate
from sympy.functions import exp
R, t = symbols('R t')
print(integrate((exp(-I*pi*R*exp(I*t)))/(2*R* \
        exp(I*t)+1)**2,(t,0,pi)))
from random import randint
maxm = 135
A = []
G = 0
G1 = 0.01
while True:
    n = randint(0,maxm)
    if n not in A:
        A.append(n)
        G = G + (-1)**n/(2*n+1)**2
    if G1!=G and abs(G-G1)/abs(G1)<10**(-4)/2:
        break
    G1 = G
    print(n, len(A), G)
print('Sum =',G)    