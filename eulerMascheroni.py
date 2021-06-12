#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 21:41:37 2021

@author: shrohanmohapatra
"""

from random import uniform
from numpy.random import exponential
from math import log
def eulerMascheroni():
    gamma = 0
    gamma1 = 0
    beta = uniform(5,100)
    A = []
    while True:
        k = int(exponential(beta))+1
        print(k,gamma,gamma1,len(A))
        if k in A: pass
        else:
            gamma = gamma + 1/k
            A.append(k)
            if len(A)>=250: break
        gamma1 = gamma
    n = max(A)
    gamma = gamma - log(n)
    return (n,gamma)
print(eulerMascheroni())
