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
    pI.append(float(x))
    pV.append(float(pVin[i]))
    i+=1
title = "Current as a function of the Source Voltage in pMOS"
yLabel = "Current"
xLabel = "Source Voltage"

[first, last, mmax, bmax, Nmax]=linefit(np.array(pV),np.array(pI))
x = np.linspace(1,2,20)
y = mmax*x+bmax
Data1 = plt.semilogy(pV, pI, 'ro', markersize=3)
labely = "Fit for WI region: y="+str(round(mmax,5))+"x+ "+str(round(bmax,5))
Data2=plt.semilogy(x, y, '-b', label=labely)
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.legend()
plt.savefig('Exp2pMOSsemi.png', format='png')
plt.show()
