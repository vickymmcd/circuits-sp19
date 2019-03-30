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


Cc = []
Vg = []

TheoCC = []
Vd = 5
Ut = 0.025

i = 0
#nMOS EKV current equation:
# I =Is log^2 (1 + e^(K(Vgb-Vto)-Vdb)/2Ut)
for x in CcRaw:
    cVal = float(x)
    vVal = float(VgRaw[i])
    Cc.append(float(CcRaw[i]))
    Vg.append(float(VgRaw[i]))
    i+=1

# [Is, Vt, Kappa] = ekvfit(np.array(Vg), np.array(Cc) )
#
# print(Is)
# print(Vt)
# print(Kappa)
#
# i = 0
# for x in Cc:
#     vVal = VgRaw[i]
#     TheoCC[i] = Is*math.log(1 + math.exp(Kappa*(vVal-Vt)-5)/2*Ut)
#     i+=1

# Setting up plot
title = "Collector Current as a function of gate voltage for an nMOS transistor"
yLabel = "Collector Current (A)"
xLabel = "Gate Voltage (V)"

# Plotting Data

Data1 = plt.semilogy(Vg, Cc, 'ro', markersize=3, label="experimental")
# Data2 = plt.semilogy(Vg, TheoCC, 'r--', markersize=3, label="EKV Model")




plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.legend()
plt.savefig('Exp1nMOS.png', format='png')
plt.show()




#
