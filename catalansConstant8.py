#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 19:11:28 2021

@author: shrohanmohapatra
"""
def catalanConstant(terms):
    G = 0
    for n in range(terms+1):
        G = G + (-1)**n/(2*n+1)**2
    return G
def decimalDigitExtractor(num):
    x = num
    for k in range(250):
        digit = int(10*x)
        print(k, digit)
        x = (10*x) - int(10*x)
decimalDigitExtractor(catalanConstant(30000))
