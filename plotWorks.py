#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 21:23:46 2021

@author: shrohanmohapatra
"""

import numpy as np
import matplotlib.pyplot as plt
nw = 100
xvals = np.linspace(0,2*nw+1,1000)
yvals = np.linspace(0,2*nw+1,1000)
x1, y1 = np.meshgrid(xvals,yvals)
f1 = x1**2+(y1-9)**2
plt.imshow(f1,origin='lower',extent=(-nw,nw,-nw,nw))