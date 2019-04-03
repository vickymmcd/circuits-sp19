# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from pmos_drain import m, b, m2, b2, m3, b3

# Isat is b
# Va is b/m
pb = b
pb2 = b2
pb3 = b3
pVa = b/m
pVa2 = b2/m2
pVa3 = b3/m3

if __name__ == '__main__':

    # Setting up plot
    title = "pMOS Early Voltage"
    xLabel = "Saturation Current (A)"
    yLabel = "Early Voltage (V)"

    # Plotting Data

    Data1 = plt.semilogx(-1*b, -1*pVa, 'ro', markersize=3, label="Vg=0V (Strong Inversion)")
    Data1 = plt.semilogx(-1*b2, -1*pVa2, 'bo', markersize=3, label="Vg=4.2V (Moderate Inversion)")
    Data1 = plt.semilogx(-1*b3, -1*pVa3, 'go', markersize=3, label="Vg=4.3V (Weak Inversion)")


    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.savefig('pmos_earlyv.png', format='png')

    plt.show()
