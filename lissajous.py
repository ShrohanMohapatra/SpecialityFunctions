#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 20:35:10 2021

@author: shrohanmohapatra
"""

import numpy as np
from random import random
from matplotlib import pyplot
x = np.linspace(-10,10,1000)
wx = round(random()*10**5)
wy = round(random()*10**5)
A = round(random()*10,3)
B = round(random()*10,3)
x = np.linspace(-A,A,1000)
alpha = round(random()*5,3)
beta = round(random()*5,3)
y = B*np.sin(wy/wx*np.arcsin(x/A)+(alpha*wy-beta*wx)/wx)
pyplot.plot(x,y)
pyplot.title('Lissajous curve \n'+ \
             'alpha = '+str(alpha)+', beta = '+str(beta)+ \
             ', A = '+str(A)+', B = '+str(B) + \
             ', wx = '+str(wx)+', wy = '+str(wy))
pyplot.show()

