# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from nmos_drain import ro, ro2, ro3, gs, gs2, gs3, b, b2, b3

# Isat is still b
# gain is ro*gs
gain = ro*gs
gain2 = ro2*gs2
gain3 = ro3*gs3

if __name__ == '__main__':

    # Setting up plot
    title = "nMOS Intrinsic Gain"
    xLabel = "Saturation Current (A)"
    yLabel = "Intrinsic Gain"

    # Plotting Data

    Data1 = plt.loglog(b, gain, 'ro', markersize=3, label="Vg=5V (Strong Inversion)")
    Data1 = plt.loglog(b2, gain2, 'bo', markersize=3, label="Vg=.8V (Moderate Inversion)")
    Data1 = plt.loglog(b3, gain3, 'go', markersize=3, label="Vg=.7V (Weak Inversion)")


    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.savefig('nmos_gain.png', format='png')
    plt.show()
