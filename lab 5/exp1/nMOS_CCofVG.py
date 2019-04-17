
import sys
sys.path.append('..')
from ekvfit import ekvfit
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats
from numpy import *
from pMOS_CCofVG import Vg2, Cc2, TheoCC2

# Importing Data-
CcRaw = open('../nmos exp1/Id.txt', 'r').read().split() #Collector Current
VgRaw = open('../nmos exp1/Vg.txt', 'r').read().split() #Gate Voltage

#[Is, Vt, Kappa] = ekvfit(Vg, Isat, 5e-4)

Cc = []
Vg = []

TheoCC = []
Vd = 5
Ut = 0.025

i = 0
#nMOS EKV current equation:
# I =Is log^2 (1 + e^(K(Vgb-Vto)-Vdb)/2Ut)


CcRaw[6] =  1e-9

thres = 0
for x in CcRaw:
    cVal = float(x)
    vVal = float(VgRaw[i])
    i+=1
    if(i > 20):
        if(thres == 4):
            Cc.append(cVal)
            Vg.append(vVal)
        thres+=1
        if(thres >4):
            thres = 0
    else:
        Cc.append(cVal)
        Vg.append(vVal)

[Is, Vt, Kappa] = ekvfit(np.array(Vg[5:60]), np.array(Cc[5:60]))


print("Is = ")
print(Is)
print("Vt = ")
print(Vt)
print("K =")
print(Kappa)

i = 0
for x in Cc:
    vVal = Vg[i]
    TheoCC.append(Is * (math.log(1 + math.exp(Kappa*(vVal-float(Vt))/(2*0.0258))))**2)
    i+=1

for i, v in enumerate(Vg2):
    Vg2[i] = v*-1

# Setting up plot
title = "Collector Current as a function of gate voltage"
yLabel = "Collector Current (A)"
xLabel = "Gate Voltage (V)"

# Plotting Data

Data1 = plt.semilogy(Vg, Cc, 'ro', markersize=3, label="experimental nMOS data")
Data2 = plt.semilogy(Vg[10:], TheoCC[10:], 'b--', markersize=3, label="EKV Model for nMOS")
Data1 = plt.semilogy(Vg2, Cc2, 'go', markersize=3, label="experimental pMOS data")
Data2 = plt.semilogy(Vg2[5:50], TheoCC2[5:50], 'k--', markersize=3, label="EKV Model for pMOS")



plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.legend()
plt.savefig('Exp1nMOS.png', format='png')
plt.show()




#
