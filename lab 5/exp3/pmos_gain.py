# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from pmos_drain import Isat, ro, Isat2, ro2, Isat3, ro3
from pmos_earlyv import Va, Va2, Va3

Is = 9.78e-8
Ut = .0258

gain = []
for i, val in enumerate(Isat):
    Isat[i] = np.exp(val)
    gain.append(-1*(np.sqrt(np.exp(val)*Is)*Va[i])/(np.exp(val)*Ut))

gain3 = []
for i, val in enumerate(Isat3):
    Isat3[i] = np.exp(val)
    gain3.append(-1*Va[i]/Ut)

if __name__ == '__main__':

    # Setting up plot
    title = "pMOS Intrinsic Gain"
    xLabel = "Saturation Current (A)"
    yLabel = "Intrinsic Gain (???)"

    # Plotting Data

    Data1 = plt.loglog(Isat, gain, 'ro', markersize=3, label="Vg=0V (Strong Inversion)")
    #Data1 = plt.semilogx(Isat2, Va2, 'bo', markersize=3, label="Vg=4.2V (Moderate Inversion)")
    Data1 = plt.semilogx(Isat3, gain3, 'go', markersize=3, label="Vg=4.3V (Weak Inversion)")


    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.show()
