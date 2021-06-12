#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 23:20:52 2021

@author: shrohanmohapatra
"""


from random import uniform
from numpy.random import normal
from math import log
def eulerMascheroni():
    gamma = 0
    gamma1 = 0
    mu = uniform(500,1000)
    sigma = 100
    A = []
    while True:
        k = int(normal(mu,sigma))
        print(k,gamma,gamma1,len(A))
        if k in A: pass
        else:
            gamma = gamma + 1/k
            A.append(k)
            if len(A)>=1000: break
        gamma1 = gamma
    n = max(A)
    gamma = gamma - log(n)
    return (n,gamma)
print(eulerMascheroni())
