# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from pmos_drain import m, b, m2, b2, m3, b3

# Isat is b
# Va is b/m
Va = b/m
Va2 = b2/m2
Va3 = b3/m3
print(b, b2, b3)

if __name__ == '__main__':

    # Setting up plot
    title = "pMOS Early Voltage"
    xLabel = "Saturation Current (A)"
    yLabel = "Early Voltage (V)"

    # Plotting Data

    Data1 = plt.semilogx(-1*b, Va, 'ro', markersize=3, label="Vg=0V (Strong Inversion)")
    Data1 = plt.semilogx(-1*b2, Va2, 'bo', markersize=3, label="Vg=4.2V (Moderate Inversion)")
    Data1 = plt.semilogx(-1*b3, Va3, 'go', markersize=3, label="Vg=4.3V (Weak Inversion)")


    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.savefig('pmos_earlyv.png', format='png')

    plt.show()
