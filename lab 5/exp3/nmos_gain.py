# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from nmos_drain import Isat, ro, Isat2, ro2, Isat3, ro3

Is = 9.78e-8

if __name__ == '__main__':

    # Setting up plot
    title = "nMOS Early Voltage"
    xLabel = "Saturation Current (A)"
    yLabel = "Early Voltage (V)"

    # Plotting Data

    Data1 = plt.semilogx(Isat, Va, 'ro', markersize=3, label="Vg=5V (Strong Inversion)")
    Data1 = plt.semilogx(Isat2, Va2, 'bo', markersize=3, label="Vg=.8V (Moderate Inversion)")
    Data1 = plt.semilogx(Isat3, Va3, 'go', markersize=3, label="Vg=.7V (Weak Inversion)")


    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.show()
