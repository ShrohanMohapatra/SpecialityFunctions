#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 15:55:58 2021

@author: shrohanmohapatra
"""

from scipy.optimize import broyden2
def paretoZeroFinder(x):
    return 5**(1+1/x)-x/(x-1)
print(broyden2(paretoZeroFinder,0.54,2500))
print(paretoZeroFinder(1.04477526717764))