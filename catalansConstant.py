#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 11:27:02 2021

@author: shrohanmohapatra
"""

from sympy import Symbol, residue, E, I, pi
z = Symbol('z')
print(residue(E**(I*pi*z)/(2*z+1)**2,z,-1/2))
from sympy import symbols, integrate
from sympy.functions import exp
R, t = symbols('R t')
print(integrate((exp(-I*pi*R*exp(I*t)))/(2*R*exp(I*t)+1)**2,(t,0,pi)))