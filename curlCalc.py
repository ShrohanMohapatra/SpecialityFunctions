#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 19:20:16 2021

@author: shrohanmohapatra
"""

from sympy.physics.vector import ReferenceFrame
from sympy.physics.vector import curl
from sympy import Function
R = ReferenceFrame('R')
psi = Function('psi')
print(curl(psi(R[0],R[1])*R.z,R))
print((-1)*curl(curl(curl(psi(R[0],R[1])*R.z,R),R),R))
