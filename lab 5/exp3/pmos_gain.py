# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from pmos_drain import ro, ro2, ro3, gs, gs2, gs3, b, b2, b3

# Isat is still b
# gain is ro*gs
pb = b
pb2 = b2
pb3 = b3
pgain = ro*gs
pgain2 = ro2*gs2
pgain3 = ro3*gs3

if __name__ == '__main__':

    # Setting up plot
    title = "pMOS Intrinsic Gain"
    xLabel = "Saturation Current (A)"
    yLabel = "Intrinsic Gain"

    # Plotting Data

    Data1 = plt.loglog(-1*pb, pgain, 'ro', markersize=3, label="Vg=0V (Strong Inversion)")
    Data1 = plt.loglog(-1*pb2, pgain2, 'bo', markersize=3, label="Vg=4.2V (Moderate Inversion)")
    Data1 = plt.loglog(-1*pb3, pgain3, 'go', markersize=3, label="Vg=4.3V (Weak Inversion)")


    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.savefig('pmos_gain.png', format='png')
    plt.show()
