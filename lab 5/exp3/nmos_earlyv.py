# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from nmos_drain import m, b, m2, b2, m3, b3

# Isat is b
# Va is b/m
Va = b/m
Va2 = b2/m2
Va3 = b3/m3

if __name__ == '__main__':

    # Setting up plot
    title = "nMOS Early Voltage"
    xLabel = "Saturation Current (A)"
    yLabel = "Early Voltage (V)"

    # Plotting Data

    Data1 = plt.semilogx(b, Va, 'ro', markersize=3, label="Vg=5V (Strong Inversion)")
    Data1 = plt.semilogx(b2, Va2, 'bo', markersize=3, label="Vg=.8V (Moderate Inversion)")
    Data1 = plt.semilogx(b3, Va3, 'go', markersize=3, label="Vg=.7V (Weak Inversion)")


    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.savefig('nmos_earlyv.png', format='png')
    plt.show()
