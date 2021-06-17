#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 18:53:58 2021

@author: shrohanmohapatra
"""

def catalanConstant(terms):
    G = 0
    for n in range(terms+1):
        G = G + (-1)**n/(2*n+1)**2
    return G
def decimalDigitExtractor(num):
    rationalNumber = []
    x = num
    for k in range(25):
        digit = int(10*x)
        rationalNumber.append(digit)
        x = (10*x) - int(10*x)
    return rationalNumber
maxNum = 25
for n in range(2,maxNum+1):
    print(n,decimalDigitExtractor(catalanConstant(n)))
