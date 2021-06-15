#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 13:05:35 2021

@author: shrohanmohapatra
"""

from random import random
from math import log, tan, pi
G = 0
err = 10**(-5)
A = []
while True:
    t = random()*pi/4
    term = (-1)*log(tan(t))
    print('Small checkpoint')
    if term in A: continue
    A.append(term)
    G1 = G
    G = G + term
    print(t,G)
    if abs(G-G1)/abs(G) < err: break
print(A, G, len(A))
print('Calculated value of Catalan%s constant',G/len(A))
