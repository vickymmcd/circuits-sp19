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

for x in nIout:
    nI.append(float(x))
    nV.append(float(nVin[i]))
    #pI.append(float(pIout[i])*-1)
    #pV.append(float(pVin[i]))
    i+=1
title = "Current as a function of the Source Voltage in nMOS"
yLabel = "Current"
xLabel = "Source Voltage"

[first, last, mmax, bmax, Nmax]=linefit(np.array(nV),np.array(nI))
x = np.linspace(1.5,3.5,2)
y = mmax*x+bmax+.0018
labely = "Fit for WI region: y="+str(round(mmax,5))+"x+ "+str(round(bmax,5)+.0018)
for i, val in enumerate(nI):
    nI[i] = -1*nI[i]
Data1 = plt.semilogy(nV, nI, 'ro', markersize=3)
print(x)
print(y)
Data2=plt.semilogy(x, y,'b', label=labely)
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.legend()
plt.savefig('Exp2nMOSsemi.png', format='png')
plt.show()




#
