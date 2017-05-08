# -*- coding: utf-8 -*-
"""
Created on Mon May 08 17:53:53 2017

@author: 214576460
"""

import numpy as np
from matplotlib import pyplot as plt
from numpy.fft import fft, ifft

def conv(f, g):
    fft1=fft(f)
    fft2=fft(g)
    
    return np.real(ifft(fft1*fft2))

def mycorr(f, g):
    xft=fft(f)
    yft1=fft(g)
    yft2=np.conjugate(yft1)
    corr=ifft(xft*yft2)
    
    return np.real(corr)

if __name__=='__main__':
    
    x=np.arange(-10, 10, 0.1)
    c=2
    y=np.exp(-0.5*x**2/c**2)
    
    correlation=mycorr(x, y)
    
    plt.plot(y, correlation)