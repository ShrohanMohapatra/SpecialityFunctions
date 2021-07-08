#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 20:39:06 2021

@author: shrohanmohapatra
"""

from sympy.abc import i, k, m, n, x
from sympy import exp, log
from sympy import Sum, factorial, oo
print(
      Sum(
          factorial(n)**3*exp(3*n)/factorial(3*n),(n,0,oo)
          ).doit().evalf())
print(Sum(
          (-1)**n*(n+1)/n**2,(n,2,oo)
          ).doit().evalf())
print(Sum(1/2**(log(n)),(n,1,oo)).doit())
