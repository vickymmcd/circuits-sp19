# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from pmos_gain import pgain, pgain2, pgain3, pb, pb2, pb3
from nmos_gain import gain, gain2, gain3, b, b2, b3

if __name__ == '__main__':

    print(pgain, pgain2, pgain3)

    # Setting up plot
    title = "Intrinsic Gain"
    xLabel = "Saturation Current (A)"
    yLabel = "Intrinsic Gain"

    # Plotting Data

    Data1 = plt.loglog(pb, pgain, 'ro', markersize=5, label="pMOS Vg=0V (Strong Inversion)")
    Data1 = plt.loglog(pb2, pgain2, 'bo', markersize=5, label="pMOS Vg=4.2V (Moderate Inversion)")
    Data1 = plt.loglog(pb3, pgain3, 'go', markersize=5, label="pMOS Vg=4.3V (Weak Inversion)")

    Data1 = plt.loglog(b, gain, 'co', markersize=5, label="nMOS Vg=5V (Strong Inversion)")
    Data1 = plt.loglog(b2, gain2, 'mo', markersize=5, label="nMOS Vg=.8V (Moderate Inversion)")
    Data1 = plt.loglog(b3, gain3, 'ko', markersize=5, label="nMOS Vg=.7V (Weak Inversion)")


    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.savefig('gain.png', format='png')
    plt.show()
