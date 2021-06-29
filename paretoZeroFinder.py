#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 12:48:33 2021

@author: shrohanmohapatra
"""

from scipy.optimize import broyden2
def paretoZeroFinder(x):
    return ((x-1)/(x-0.8))**x - 0.2
# print(newton_krylov(paretoZeroFinder,7.21))
print(paretoZeroFinder(1.9484046685235312))
print(broyden2(paretoZeroFinder,1.95,1000))
print(paretoZeroFinder(1.0556605455704873))
