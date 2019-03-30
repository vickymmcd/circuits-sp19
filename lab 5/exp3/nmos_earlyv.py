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

Ilogged = []
Ilogged2 = []
Ilogged3 = []

Vd = []
Vd2 = []
Vd3 = []

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
    if Iraw[i] > 0:
        Ilogged.append(np.log(Iraw[i]))
        Vd.append(VdRaw[i])
    i+=1
    #TheoCC = #EQUATION

i = 0
for x in Iraw2:
    Iraw2[i] = float(Iraw2[i])
    VdRaw2[i] = float(VdRaw2[i])
    if Iraw[i] > 0:
        Ilogged2.append(np.log(Iraw2[i]))
        Vd2.append(VdRaw2[i])
    i+=1

i = 0
for x in Iraw3:
    Iraw3[i] = float(Iraw3[i])
    VdRaw3[i] = float(VdRaw3[i])
    if Iraw[i] > 0:
        Ilogged3.append(np.log(Iraw3[i]))
        Vd3.append(VdRaw3[i])
    i+=1

# we know that gs = slope of drain characteristic deep in the ohmic region
# slope = rise/run = delta y / delta x
gs = (Ilogged[1] - Ilogged[0]) / (Vd[1] - Vd[0])
gs2 = (Ilogged2[1] - Ilogged2[0]) / (Vd2[1] - Vd2[0])
gs3 = (Ilogged3[1] - Ilogged3[0]) / (Vd3[1] - Vd3[0])

# we know that 1/ro = slope of drain characteristic deep in saturation
#first, last, mmax, bmax, Nmax = linefit(np.array(Ilogged[50:]), np.array(Vd[50:]))
#print(first, last, mmax, bmax, Nmax)
inversero = (Ilogged[55] - Ilogged[54]) / (Vd[55] - Vd[54])
ro = 1/inversero
inversero = (Ilogged2[55] - Ilogged2[54]) / (Vd2[55] - Vd2[54])
ro2 = 1/inversero
inversero = (Ilogged3[55] - Ilogged3[54]) / (Vd3[55] - Vd3[54])
ro3 = 1/inversero

if __name__ == '___main__':
    print(ro, ro2, ro3)
    print(gs, gs2, gs3)

    # Setting up plot
    title = "nMOS Drain Characteristic"
    yLabel = "Channel Current (A)"
    xLabel = "Drain Voltage (V)"

    # Plotting Data

    Data1 = plt.semilogy(VdRaw, Iraw, 'ro', markersize=3, label="Vg=5V (Strong Inversion)")
    Data1 = plt.semilogy(VdRaw2, Iraw2, 'go', markersize=3, label="Vg=.8V (Moderate Inversion)")
    Data1 = plt.semilogy(VdRaw3, Iraw3, 'bo', markersize=3, label="Vg=.7V (Weak Inversion)")

    #Data2 = plt.semilogy(Vg, TheoCC 'r--', markersize=3, label="EKV Model")

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.show()
