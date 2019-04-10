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

[Is, Vt, Kappa] = ekvfit(Vg, Isat, 5e-4)

Cc = []
Vg = []

TheoCC = []


k = 1.381e-23
#Is = ??
#Ut = ??

#nMOS EKV current equation:
# I =Is e^(κ(Vg-Vto)/Ut) * (e^(-Vs/Ut) -e^(-Vd/Ut))


i = 0
for x in CcRaw:
    cVal = float(x)
    vVal = float(VgRaw[i])
    CcRaw[i] = float(CcRaw[i])
    VgRaw[i] = float(VgRaw[i])
    i+=1
    #TheoCC = #EQUATION

# Setting up plot
title = "Collector Current as a function of gate voltage for an nMOS transistor"
yLabel = "Collector Current (A)"
xLabel = "Gate Voltage (V)"

# Plotting Data

Data1 = plt.semilogy(VgRaw, CcRaw, 'ro', markersize=3, label="experimental")
#Data2 = plt.semilogy(Vg, TheoCC 'r--', markersize=3, label="EKV Model")

plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.legend()
plt.savefig('Exp1nMOS.png', format='png')
plt.show()




#
