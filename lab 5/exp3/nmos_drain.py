# -*- coding: utf-8 -*-

import sys
sys.path.append('..')
from ekvfit import ekvfit
from linefit import linefit
import numpy as np
import matplotlib.pyplot as plt

# Importing Data
Iraw = open('../nmos exp3 5/Id.txt', 'r').read().split()
VdRaw = open('../nmos exp3 5/Vd.txt', 'r').read().split()
Iraw2 = open('../nmos exp3 .8/Id.txt', 'r').read().split()
VdRaw2 = open('../nmos exp3 .8/Vd.txt', 'r').read().split()
Iraw3 = open('../nmos exp3 .7/Id.txt', 'r').read().split()
VdRaw3 = open('../nmos exp3 .7/Vd.txt', 'r').read().split()

I = []
Vg = []

TheoCC = []


k = 1.381e-23
#Is = ??
#Ut = ??

#nMOS EKV current equation:
# I =Is e^(κ(Vg-Vto)/Ut) * (e^(-Vs/Ut) -e^(-Vd/Ut))


i = 0
for x in Iraw:
    cVal = float(x)
    vVal = float(VdRaw[i])
    Iraw[i] = float(Iraw[i])
    VdRaw[i] = float(VdRaw[i])
    i+=1
    #TheoCC = #EQUATION

i = 0
for x in Iraw2:
    Iraw2[i] = float(Iraw2[i])
    VdRaw2[i] = float(VdRaw2[i])
    i+=1

i = 0
for x in Iraw3:
    Iraw3[i] = float(Iraw3[i])
    VdRaw3[i] = float(VdRaw3[i])
    i+=1

# we know that gs = slope of drain characteristic deep in the ohmic region
[first, last, mmax, bmax, Nmax] = linefit(np.array(VdRaw[0:5]), np.array(Iraw[0:5]))
print([first, last, mmax, bmax, Nmax])

# Setting up plot
title = "nMOS Drain Characteristic"
yLabel = "Channel Current (A)"
xLabel = "Drain Voltage (V)"

# Plotting Data

Data1 = plt.semilogy(VdRaw[0:5], Iraw[0:5], 'ro', markersize=3, label="Vg=5V (Strong Inversion)")
#Data1 = plt.semilogy(VdRaw2, Iraw2, 'go', markersize=3, label="Vg=.8V (Moderate Inversion)")
#Data1 = plt.semilogy(VdRaw3, Iraw3, 'bo', markersize=3, label="Vg=.7V (Weak Inversion)")

#Data2 = plt.semilogy(Vg, TheoCC 'r--', markersize=3, label="EKV Model")

plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.legend()
plt.savefig('Exp3nMOS.png', format='png')
plt.show()
