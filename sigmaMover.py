#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 19:29:31 2021

@author: shrohanmohapatra
"""

import matplotlib.pyplot as plt
import numpy as np
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage
duration = 20
c = 50
sigma = 100
x = np.linspace(0, c*duration, 1000)
fig, ax = plt.subplots()
def make_frame(t):
    ax.clear()
    ax.plot(x,np.exp(-(x-c*t)**2/(2*sigma**2)),lw=3)
    ax.set_ylim(-0.1, 1.1)
    return mplfig_to_npimage(fig)
animation = VideoClip(make_frame, duration = duration)
animation.ipython_display(fps = 25, loop = True, autoplay = True)