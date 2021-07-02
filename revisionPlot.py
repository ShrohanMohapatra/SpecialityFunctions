#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 19:51:25 2021

@author: shrohanmohapatra
"""

import numpy as np
from matplotlib import pyplot
xData1 = np.linspace(0,10,10)
yData1 = 3 - xData1
yData2 = (4 - xData1)/2
yData3 = (9-2*xData1)/5
pyplot.plot(xData1,yData1)
pyplot.plot(xData1,yData2)
pyplot.plot(xData1,yData3)
pyplot.xlabel('X-axis')
pyplot.ylabel('Y-axis')
