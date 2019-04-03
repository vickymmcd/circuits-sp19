import sys
sys.path.append('..')
from linefit import linefit
from scipy import stats
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
    pI.append(float(pIout[i]))
    pV.append(float(pVin[i]))
    i+=1
title = "Current as a function of the Source Voltage in nMOS"
yLabel = "Current (A)"
xLabel = "Source Voltage (V)"
pIlog = []
for i, val in enumerate(pI):
    pIlog.append(np.log(val))
slope, intercept, r_value, p_value, std_err = stats.linregress(pV[30:40], pIlog[30:40])

x = np.array(pV[30:40])
y = np.exp(slope*x+intercept)

nIlog = []
for i, val in enumerate(nI):
    nIlog.append(np.log(val))
slope1, intercept1, r_value, p_value, std_err = stats.linregress(nV[50:60], nIlog[50:60])
print(len(nV))
x1 = np.array(nV[50:60])
y1 = np.exp(slope1*x1+intercept1)

print(x)
print(y)
labely = "Fit for pMOS WI region: y="+str(round(slope,5))+"x+ "+str(round(intercept,5))
Data1 = plt.semilogy(pV, pI, 'mo', markersize=3,label='pMOS')
Data2=plt.semilogy(x, y,'g-', label=labely)
Data1 = plt.semilogy(nV, nI, 'ro', markersize=3,label='nMOS')
labely = "Fit for nMOS WI region: y="+str(round(slope1,5))+"x+ "+str(round(intercept1,5))
Data2=plt.semilogy(x1, y1, 'b-', label=labely)
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.legend()
plt.savefig('Exp2nMOSsemi.png', format='png')
plt.show()




#
