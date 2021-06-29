#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 13:24:52 2021

@author: shrohanmohapatra
"""
from matplotlib import pyplot
import numpy as np
from random import random
def paretoPrinciple(xm,a,x):
    return 1-(xm/x)**a
xm = random()*100
alpha = 1.0556605
xData1 = np.linspace(xm,20*xm,10**4)
yData1 = paretoPrinciple(xm, alpha, xData1)
xData2 = np.ones(10**4)*(xm*((alpha-0.8)/(alpha-1)))
yData2 = np.linspace(0.0,1.0,10**4)
xData3 = np.ones(10**4)*(xm*(alpha/(alpha-1)))
yData3 = np.ones(10**4)*0.8
fig = pyplot.figure()
pyplot.plot(xData1, yData1)
pyplot.plot(xData2, yData2)
pyplot.plot(xData3, yData2)
pyplot.plot(xData1, yData3)
pyplot.show()
print('xm = ',xm)
print('pointerAt8020 = ',(alpha-0.8)/(alpha-1))
print('mean = ',alpha/(alpha-1))
print('pointerAt8020/mean = ',(alpha-0.8)/alpha*100,'%')

