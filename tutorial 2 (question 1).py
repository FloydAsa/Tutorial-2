# -*- coding: utf-8 -*-
"""
Created on Mon May 08 17:54:33 2017

@author: 214576460
"""

import numpy as np
from matplotlib import pyplot as plt
from numpy.fft import fft, ifft

def conv(f, g):
    fft1=fft(f)
    fft2=fft(g)
    
    return np.real(ifft(fft1*fft2))

def shift(x, dx=0):
    vec=np.zeros(len(x))
    vec[dx]=1
    xft=conv(x, vec)
    
    return xft


if __name__=='__main__':
    
    x=np.arange(-10, 10, 0.1)
    c=2
    y=np.exp(-0.5*x**2/c**2)
    #print y
    yshift=shift(y,y.size/2)
    #print yshift
    
    #plt.plot(x,y)
    plt.plot(y, yshift)