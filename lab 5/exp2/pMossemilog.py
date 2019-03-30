import sys
sys.path.append('..')
from linefit import linefit
#from ekvfit import ekvfit
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats
nIout = open('nmosexp2/Iout.txt', 'r').read().split()
nVin = open('pmosexp2/Vin.txt', 'r').read().split()
pIout = open('pmosexp2/Iout.txt', 'r').read().split()
pVin = open('pmosexp2/Vin.txt', 'r').read().split()
nI=[]
nV=[]
pI=[]
pV=[]
i = 0

for x in pIout:
    #nI.append(float(x))
    #nV.append(float(nVin[i]))
    pI.append(float(x)*-1)
    pV.append(float(pVin[i]))
    i+=1
title = "Current as a function of the Source Voltage in nMOS"
yLabel = "Current"
xLabel = "Source Voltage"

[first, last, mmax, bmax, Nmax]=linefit(np.array(pV),np.array(pI))
x = np.logspace(.25,.55,2)
y = mmax*x+bmax

Data1 = plt.semilogx(pV, pI, 'ro', markersize=3)
Data2=plt.semilogx(x, y, '-r', label='best fit')
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.legend()
plt.savefig('Exp2nMOSsemi.png', format='png')
plt.show()
