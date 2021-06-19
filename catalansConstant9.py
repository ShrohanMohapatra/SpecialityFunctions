#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 20:35:38 2021

@author: shrohanmohapatra
"""

from scipy.special import zeta
nmax = 20
for n in range(1,nmax+1):
    print("n = ",n,zeta(2*n+1))
    print(n*zeta(2*n+1),16**n)