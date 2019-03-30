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

[ss,s,sss,kk,k]=linefit(np.array(nV),np.array(nI))
Data1 = plt.semilogx(nV, nI, 'ro', markersize=3)
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.legend()
plt.savefig('Exp2nMOSsemi.png', format='png')
plt.show()




#