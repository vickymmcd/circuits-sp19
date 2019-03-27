import sys
sys.path.append('..')
from linefit import linefit
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats

nIout = open('../nmosexp2/Iout.txt', 'r').read().split()
nVin = open('../nmosexp2/Vin.txt', 'r').read().split()
pIout = open('../pmosexp2/Iout.txt', 'r').read().split()
pVin = open('../pmosexp2/Vin.txt', 'r').read().split()
nI=[]
nV=[]
pI=[]
pV=[]
i = 0
for x in nIout:
    nI[i] = float(x)
    nV[i] = float(nVin[i])
    pI[i] = float(pIout[i])
    pV[i] = float(pVin[i])
    i+=1


# title = "Collector Current as a function of gate voltage for an nMOS transistor"
# yLabel = "Collector Current (A)"
# xLabel = "Gate Voltage (V)"
# Data1 = plt.semilogy(VgRaw, CcRaw, 'ro', markersize=3, label="experimental")
# plt.xlabel(xLabel)
# plt.ylabel(yLabel)
# plt.title(title)
# plt.legend()
# plt.savefig('Exp1nMOS.png', format='png')
# plt.show()




#
