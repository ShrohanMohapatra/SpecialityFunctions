#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 13:41:53 2021

@author: shrohanmohapatra
"""


import numpy as np
from matplotlib import pyplot
xData1 = np.linspace(0,10,10)
yData1 = 3*xData1+0.5*8*xData1**2
pyplot.plot(xData1,yData1)
pyplot.xlabel('X-axis')
pyplot.ylabel('Y-axis')
