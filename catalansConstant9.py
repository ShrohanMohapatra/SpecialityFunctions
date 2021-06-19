#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 20:35:38 2021

@author: shrohanmohapatra
"""

from scipy.special import zeta
nmax = 5
for n in range(1,nmax+1):
    print("n = ",n,zeta(2*n+1))
    print(n*zeta(2*n+1),16**n)
# E W Weisstein Sept 30 2007
A = [1/(k+1)**2 for k in range(24*nmax+22)]
G = 0
print(A)
print("Computing the Catalan's constant ...")
for k in range(nmax):
    G1 = G
    p = 1/2048/4096**k
    p1 = 12288*A[24*k+4]-768*A[24*k+5]+9216*A[24*k+6]+10368*A[24*k+8]
    p1 = p1 + 3072*A[24*k+1]-3072*A[24*k+2]-23040*A[24*k+3]
    p1 = p1 + 2496*A[24*k+9] - 192*A[24*k+10] + 768*A[24*k+12]
    p1 = p1 - 48*A[24*k+13] + 360*A[24*k+15] + 648*A[24*k+16]
    p1 = p1 + 12*A[24*k+17] + 168*A[24*k+18] + 48*A[24*k+20]
    p1 = p1 - 39*A[24*k+21]
    G = G + p1*p
    print(abs(G-G1)/abs(G))
print('Catalan\'s constant = ',1+G)