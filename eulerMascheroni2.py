#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 19:45:44 2021

@author: shrohanmohapatra
"""

from random import uniform
from math import log
def eulerMascheroni():
    gamma = 0
    gamma1 = 0
    A = []
    while True:
        k = int(uniform(1, 10000))
        print(k,gamma,gamma1,len(A))
        if k in A: pass
        else:
            gamma = gamma + 1/k
            A.append(k)
            if len(A)>=8000: break
        gamma1 = gamma
    n = max(A)
    gamma = gamma - log(n)
    return (n,gamma)
print(eulerMascheroni())
