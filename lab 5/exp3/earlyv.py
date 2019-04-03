# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from pmos_earlyv import pVa, pVa2, pVa3, pb, pb2, pb3
from nmos_earlyv import Va, Va2, Va3, b, b2, b3


if __name__ == '__main__':

    print(pVa, pVa2, pVa3)
    print(pb, pb2, pb3)

    # Setting up plot
    title = "Early Voltage"
    xLabel = "Saturation Current (A)"
    yLabel = "Early Voltage (V)"

    # Plotting Data

    Data1 = plt.semilogx(pb, pVa, 'ro', markersize=5, label="pMOS Vg=0V (Strong Inversion)")
    Data1 = plt.semilogx(pb2, pVa2, 'bo', markersize=5, label="pMOS Vg=4.2V (Moderate Inversion)")
    Data1 = plt.semilogx(pb3, pVa3, 'go', markersize=5, label="pMOS Vg=4.3V (Weak Inversion)")

    Data1 = plt.semilogx(b, Va, 'co', markersize=5, label="nMOS Vg=5V (Strong Inversion)")
    Data1 = plt.semilogx(b2, Va2, 'mo', markersize=5, label="nMOS Vg=.8V (Moderate Inversion)")
    Data1 = plt.semilogx(b3, Va3, 'ko', markersize=5, label="nMOS Vg=.7V (Weak Inversion)")


    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.savefig('earlyv.png', format='png')

    plt.show()
