#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 19:49:58 2021

@author: shrohanmohapatra
"""

from sympy import symbols, simplify
x = symbols('x')
print(simplify(x**2+2*x+1-(x+1)**2))