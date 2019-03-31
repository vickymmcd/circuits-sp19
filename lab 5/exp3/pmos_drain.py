# -*- coding: utf-8 -*-

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Importing Data
Iraw = open('../pmos exp3 0/Id.txt', 'r').read().split()
VdRaw = open('../pmos exp3 0/Vd.txt', 'r').read().split()
Iraw2 = open('../pmos exp3 4.2/Id.txt', 'r').read().split()
VdRaw2 = open('../pmos exp3 4.2/Vd.txt', 'r').read().split()
Iraw3 = open('../pmos exp3 4.3/Id.txt', 'r').read().split()
VdRaw3 = open('../pmos exp3 4.3/Vd.txt', 'r').read().split()

Ilogged = []
Ilogged2 = []
Ilogged3 = []

Vd = []
Vd2 = []
Vd3 = []

Vsat = []
Isat = []
Vsat2 = []
Isat2 = []
Vsat3 = []
Isat3 = []


#Is = ??
#Ut = ??


i = 0
for x in Iraw:
    cVal = float(x)
    vVal = float(VdRaw[i])
    Iraw[i] = -1*float(Iraw[i])
    VdRaw[i] = float(VdRaw[i])
    if Iraw[i] > 0:
        Ilogged.append(np.log(Iraw[i]))
        Vd.append(VdRaw[i])
        if VdRaw[i] < 2.0:
            Vsat.append(VdRaw[i])
            Isat.append(np.log(Iraw[i]))
    i+=1


i = 0
for x in Iraw2:
    Iraw2[i] = -1*float(Iraw2[i])
    VdRaw2[i] = float(VdRaw2[i])
    if Iraw[i] > 0:
        Ilogged2.append(np.log(Iraw2[i]))
        Vd2.append(VdRaw2[i])
        if VdRaw2[i] < 2.0:
            Vsat2.append(VdRaw2[i])
            Isat2.append(np.log(Iraw2[i]))
    i+=1

i = 0
for x in Iraw3:
    Iraw3[i] = -1*float(Iraw3[i])
    VdRaw3[i] = float(VdRaw3[i])
    if Iraw[i] > 0:
        Ilogged3.append(np.log(Iraw3[i]))
        Vd3.append(VdRaw3[i])
        if VdRaw3[i] < 2.0:
            Vsat3.append(VdRaw3[i])
            Isat3.append(np.log(Iraw3[i]))
    i+=1

slope2, intercept2, r_value, p_value, std_err = stats.linregress(Vsat, Isat)
ro = 1/slope2

slope2, intercept2, r_value, p_value, std_err = stats.linregress(Vsat2, Isat2)
ro2 = 1/slope2

slope2, intercept2, r_value, p_value, std_err = stats.linregress(Vsat3, Isat3)
ro3 = 1/slope2
Vsat = np.array(Vsat)
Vsat2 = np.array(Vsat2)
Vsat3 = np.array(Vsat3)

if __name__ == '__main__':

    # Setting up plot
    title = "pMOS Drain Characteristic"
    yLabel = "Channel Current (A)"
    xLabel = "Drain Voltage (V)"

    # Plotting Data

    Data1 = plt.semilogy(VdRaw, Iraw, 'ro', markersize=3, label="Vg=0V (Strong Inversion)")
    Data1 = plt.semilogy(VdRaw2, Iraw2, 'go', markersize=3, label="Vg=4.2V (Moderate Inversion)")
    Data1 = plt.semilogy(VdRaw3, Iraw3, 'bo', markersize=3, label="Vg=4.3V (Weak Inversion)")
    #Data = plt.plot(Vsat3, np.exp(slope2*(Vsat3)+intercept2), 'r', label="fitted line: y=e^("+str(round(slope2, 5))+"x + " +str(round(intercept2, 5)) + ")")
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.show()
