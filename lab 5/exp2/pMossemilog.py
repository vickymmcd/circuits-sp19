import sys
sys.path.append('..')
from linefit import linefit
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
print (pIout)
print(pVin)
for x in nIout:
    #nI.append(float(x)*-1)
    #nV.append(float(nVin[i]))
    pI.append(float(pIout[i])*-1)
    pV.append(float(pVin[i]))
    i+=1
print (pV)
print (pI)
title = "Current as a function of the Source Voltage in pMOS"
yLabel = "Current"
xLabel = "Source Voltage"
Data1 = plt.semilogx(pV, pI, 'ro', markersize=3)
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.legend()
plt.savefig('Exp2nMOSsemi.png', format='png')
plt.show()
