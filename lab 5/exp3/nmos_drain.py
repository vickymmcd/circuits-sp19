# -*- coding: utf-8 -*-

import sys
sys.path.append('..')
from ekvfit import ekvfit
from linefit import linefit
import numpy as np
from scipy import stats
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

Vsat = []
Isat = []

Iextra = []
Vextra = []


k = 1.381e-23
#Is = ??
#Ut = ??

#nMOS EKV current equation:
# I =Is e^(κ(Vg-Vto)/Ut) * (e^(-Vs/Ut) -e^(-Vd/Ut))

counter = 0
i = 0
for x in Iraw:
    cVal = float(x)
    vVal = float(VdRaw[i])
    Iraw[i] = float(Iraw[i])
    VdRaw[i] = float(VdRaw[i])
    if Iraw[i] > 0:
        Ilogged.append(np.log(Iraw[i]))
        Vd.append(VdRaw[i])
        if VdRaw[i] > 1.5:
            Vsat.append(VdRaw[i])
            Isat.append(np.log(Iraw[i]))
    if i > 40:
        if counter == 4:
            Iextra.append(Iraw[i])
            Vextra.append(VdRaw[i])
            counter = 0
        counter+=1
    else:
        Iextra.append(Iraw[i])
        Vextra.append(VdRaw[i])
    i+=1


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

#Is, VT, kappa = ekvfit(np.array(Vextra[1:]), np.array(Iextra[1:]))
# heoCC = []
# for vval in Vextra[1:]:
#     heoCC.append(Is * (np.log(1 + np.exp(kappa*(vVal-float(VT))/(2*0.0258))))**2)
#print(Is, VT, kappa)
slope, intercept, r_value, p_value, std_err = stats.linregress(Vd[:5], Ilogged[:5])

slope2, intercept2, r_value, p_value, std_err = stats.linregress(Vsat, Isat)
Vsat = np.array(Vsat)
print(Vsat)

if __name__ == '__main__':
    print(ro, ro2, ro3)
    print(gs, gs2, gs3)

    # Setting up plot
    title = "nMOS Drain Characteristic"
    yLabel = "Channel Current (A)"
    xLabel = "Drain Voltage (V)"

    # Plotting Data

    Data1 = plt.semilogy(Vextra, Iextra, 'ro', markersize=3, label="Vg=5V (Strong Inversion)")
    Data1 = plt.semilogy(VdRaw2, Iraw2, 'go', markersize=3, label="Vg=.8V (Moderate Inversion)")
    Data1 = plt.semilogy(VdRaw3, Iraw3, 'bo', markersize=3, label="Vg=.7V (Weak Inversion)")
    Data = plt.plot(Vsat, np.exp(slope2*(Vsat)+intercept2), 'r', label="fitted line: y=e^("+str(round(slope2, 5))+"x + " +str(round(intercept2, 5)) + ")")
    #Data = plt.plot(Vd[:5], np.exp(slope*(np.array(Vd[:5]))+intercept), 'r', label="fitted line: y=e^("+str(round(slope, 5))+"x + " +str(round(intercept, 5)) + ")")
    #Data = plt.plot(Vextra[1:], heoCC, 'b', label="hi")

    #Data2 = plt.semilogy(Vg, TheoCC 'r--', markersize=3, label="EKV Model")

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.show()
