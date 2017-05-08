# -*- coding: utf-8 -*-
"""
Created on Mon May 08 18:01:49 2017

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
    

#question 2

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

#Question 3
#using the already shifted gaussian from question 1 we will have:
#print yshift
correlationyshift=mycorr(y, yshift)

plt.plot(x, correlation)
plt.plot(x, correlationyshift)

#QUestion 4
#wrap aound errors are overcome by zero padding say an image or an N by N matrice and convolving it to twice its size

#to pad the two matrices with zeros we have
def pad(x):
    xx=np.zeros(2*len(x))
    xx[0:x.size]=x
    
    return xx

if __name__=='__main__':
    
    x=np.arange(-10, 10, 0.1)
    x1=pad(x)
    #print x1, len(x1)
    c=2
    y=np.exp(-0.5*x**2/c**2)
    y1=pad(y)
    #print y1, len(y1)
    
    ywrap=conv(x1, y1)
    #print ywrap, len(ywrap)
    
    
