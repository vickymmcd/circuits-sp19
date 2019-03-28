# -*- coding: utf-8 -*-

#Script to semilog-plot the channel current as a function of gate voltage of nMOS transistor
#Extracts Is, κ, and VT0
#Plots theoretical EKV model
import sys
sys.path.append('..')
from ekvfit import ekvfit
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats

# Importing Data
CcRaw = open('../nmos exp1/Id.txt', 'r').read().split() #Collector Current
VgRaw = open('../nmos exp1/Vg.txt', 'r').read().split() #Gate Voltage
pCcRaw = open('../pmos exp1/Id.txt', 'r').read().split() #Collector Current
pVgRaw = open('../pmos exp1/Vg.txt', 'r').read().split() #Gate Voltage


Cc = []
Vg = []

pCc = []
pVg = []

gmnMos = []
gmpMos = []

nTheoCC = []
pTheoCC = []

Vd = 5
Ut = 0.025

i = 0
for x in CcRaw:
    cVal = float(x)
    vVal = float(VgRaw[i])
    Cc.append(float(CcRaw[i]))
    Vg.append(float(VgRaw[i]))
    i+=1

i = 0
for x in pCcRaw:
    cVal = float(x)
    vVal = float(pVgRaw[i])
    pCc.append(float(pCcRaw[i]))
    pVg.append(float(pVgRaw[i]))
    i+=1

nVgDiff = []
nVgDiffraw = np.diff(Vg)
nCcDiff = []

i = 0
for x in nVgDiffraw:
    if(x == 0):
        nVgDiff.append(0.057)
    else:
        nVgDiff.append(x)
    nCcDiff.append(Cc[i])
    i+=1

gmnMos = np.divide(nCcDiff,nVgDiff)  # delta Isat over delta Vg

pVgDiff = []
pVgDiffraw = np.diff(pVg)
pCcDiff = []

i = 0
for x in pVgDiffraw:
    if(x == 0):
        pVgDiff.append(0.057)
    else:
        pVgDiff.append(x)
    pCcDiff.append(Cc[i])
    i+=1

gmpMos = np.divide(pCcDiff,pVgDiff)  # delta Isat over delta Vg

# i = 0
# for x in Cc:
#     vVal = VgRaw[i]
#     TheoCC[i] = Is*math.log(1 + math.exp(Kappa*(vVal-Vt)-5)/2*Ut)
#     i+=1

# Setting up plot
title = "Incremental Transconductance Gain (gm) vs Isat"
yLabel = "gm (mho)"
xLabel = "Isat (I)"

# Plotting Data

Data1 = plt.loglog(Cc[0:59], gmnMos, 'ro', markersize=3, label="nMOS gm")
Data2 = plt.loglog(Cc[0:59], gmpMos, 'bo', markersize=3, label="pMOS gm")

# Data2 = plt.semilogy(Vg, TheoCC, 'r--', markersize=3, label="EKV Model")




plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.legend()
plt.savefig('Exp1Gm.png', format='png')
plt.show()




#
