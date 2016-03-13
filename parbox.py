#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = "Muammar El Khatib."
__copyright__ = "Copyright 2016, Muammar El Khatib."
__credits__ = [""]
__license__ = "GPL"
__version__ = "3"
__maintainer__ = "Muammar El Khatib"
__email__ = "muammarelkhatib@gmail.com"
__status__ = "Development"
"""


L=input('Enter size of the box: ')
L=float(L)

npoints=input('Enter number of points: ')
npoints=int(npoints)

print ('Size of the Box:', L)
print ('Number of points:', npoints)

n=input('Enter number of n: ')
n=int(n)

nstep=L/npoints
print ('step:', nstep)

import pylab as pl

x=pl.frange(0,L,nstep)
print (x)

# Calculation of the wave function
import math
wfarray=[]
xarray=[]
darray=[]
tpsarray=[]
expecpp=[]
expecpp2=[]
for i in x:
    wf=math.sqrt((2/L))*math.sin(((n*math.pi*i)/L))
    wfarray.append(wf)
    xarray.append(i)
    darray.append(wf**2)
    tpsarray.append((i*wf**2)**2)
    expecpp.append(i*wf**2)
    expecpp2.append(i**2*wf**2)
    print (i, wf, wf**2)


#print ('Expectation value of position: ', sum(expecpp)/npoints)
#print ('Expectation value of position: ', sum(darray))
#print ('tps: ', sum(darray)-sum(expecpp))

import matplotlib.pyplot as plt
plt.plot(xarray,wfarray)
plt.show()

plt.plot(xarray,darray)
plt.show()

plt.plot(xarray,tpsarray)
plt.show()
