#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 13:48:44 2021

@author: shrohanmohapatra
"""

from random import uniform, random
# Just verifying the order of simplifying the expression
x = uniform(3, 4)
y = uniform(3, 4)
print(x, y, x**2, y**2, x**2*y**2)
# Computing the Catalan's constant using Monte Carlo in 2D ....
G, err, A = 0, 10**(-4), []
while True:
    x = random()
    y = random()
    if (x,y) in A: continue
    A.append((x,y))
    G1 = G
    G = G + 1/(1+x**2*y**2)
    if abs(G-G1)/abs(G1+10**(-6))<err: break
print('Length of the array',len(A))
print('Calculation of Catalans constant',G/len(A))