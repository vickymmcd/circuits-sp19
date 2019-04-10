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
pCcRaw = open('../pmos exp1-2/Id.txt', 'r').read().split() #Collector Current
pVgRaw = open('../pmos exp1-2/Vg.txt', 'r').read().split() #Gate Voltage


Cc = []
Vg = []

pCc = []
pVg = []

gmnMos = []
gmpMos = []

nTheoCC = []
pTheoCC = []

Vd = 5
Ut = 0.0258

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

# print(pCc[18])
# print(pCc[21])
# # gmnMos[29] = gmnMos[30]
# # gmpMos[19] = gmpMos[20]

nVgDiff = []
nVgDiffraw = np.diff(Vg)
nCcDiff = []

i = 0
for x in nVgDiffraw:
    if(x == 0):
        nVgDiff.append(nVgDiff[i-1])
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
        pVgDiff.append(pVgDiff[i-1])
    else:
        pVgDiff.append(x)
    pCcDiff.append(Cc[i])
    i+=1

gmpMos = np.divide(pCcDiff,pVgDiff)  # delta Isat over delta Vg


i = 0
for x in Vg:
    i+=1
    nTheoCC.append(9.78176739226e-08 * (math.log(1 + math.exp(2.8528*(x-float(0.609))/(2*0.0258))))**2)

i = 0
for x in pVg:
    i+=1
    # pTheoCC.append(1.56109 * (math.log(1 + math.exp(0.3636*(x-float(-3.53489))/(2*0.0258))))**2)
    pTheoCC.append((1.5* (math.log(1 + math.exp(0.3636*(x-float(3.53489))/(2*0.0258))))**2)/1e5)

nVgDiffTheo = []
nVgDiffrawTheo = np.diff(Vg)
nCcDiffTheo = []

i = 0
for x in nVgDiffrawTheo:
    if(x == 0):
        nVgDiffTheo.append(nVgDiffTheo[i-1])
    else:
        nVgDiffTheo.append(x)
    nCcDiffTheo.append(nTheoCC[i])
    i+=1

gmnMosTheo = np.divide(nCcDiffTheo,nVgDiffTheo)  # delta Isat over delta Vg

pVgDiffTheo = []
pVgDiffrawTheo = np.diff(Vg)
pCcDiffTheo = []

# o = 0
# for m in pTheoCC:
#     pTheoCC[o] = m
#     o+=1

i = 0
for x in pVgDiffrawTheo:
    if(x == 0):
        pVgDiffTheo.append(pVgDiffTheo[i-1])
    else:
        pVgDiffTheo.append(x)
    pCcDiffTheo.append(pTheoCC[i])
    i+=1

gmpMosTheo = np.divide(pCcDiffTheo,pVgDiffTheo)  # delta Isat over delta Vg
# i = 0
# for x in Cc:
#     vVal = VgRaw[i]
#     TheoCC[i] = Is*math.log(1 + math.exp(Kappa*(vVal-Vt)-5)/2*Ut)
#     i+=1

# Setting up plot
title = "Incremental Transconductance Gain (gm) vs Isat"
yLabel = "gm (mho)"
xLabel = "Isat (I)"

# gmnMos[29] = gmnMos[30]
# gmpMos[19] = gmpMos[20]

# Plotting Data

print(gmpMosTheo)

Data1 = plt.loglog(Cc[0:59], gmnMos, 'ro', markersize=3, label="nMOS gm")
Data2 = plt.loglog(Cc[0:59], gmpMos, 'bo', markersize=3, label="pMOS gm")
Data3 = plt.loglog(nTheoCC[11:59], gmnMosTheo[11:], 'r--', markersize=3, label="nMOS gm Theoretical")
Data4 = plt.loglog(pTheoCC[25:59], gmpMosTheo[25:], 'b--', markersize=3, label="pMOS gm Theoretical")

# Data2 = plt.semilogy(Vg, TheoCC, 'r--', markersize=3, label="EKV Model")




plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.legend()
plt.savefig('Exp1Gm.png', format='png')
plt.show()




#
