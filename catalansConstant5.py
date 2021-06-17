#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 18:00:34 2021

@author: shrohanmohapatra
"""

def decimalDigitExtractor(num):
    rationalNumber = []
    decimalNumber = 1.0/(num+0.0)
    x = decimalNumber
    for k in range(15):
        digit = int(10*x)
        if digit not in rationalNumber:
            rationalNumber.append(digit)
        x = (10*x) - int(10*x)
        #print('x = ',x,'digit = ',digit)
    if len(rationalNumber) == 10:
        for k in range(15):
            digit = int(10*x)
            if digit not in rationalNumber:
                rationalNumber.append(digit)
            x = (10*x) - int(10*x)
            #print('x = ',x,'digit = ',digit)
    return rationalNumber
maxNum = 25
for n in range(1,maxNum+1):
    print(n,(2*n-1)**2,1.0/(2*n-1)**2)
    f = decimalDigitExtractor((2*n-1)**2)
    print(n,(2*n-1)**2,f,len(f))