# -*- coding: utf-8 -*-

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from exp2vdd import Iraw3, VdRaw3, Iraw, VdRaw
from exp2_10mv import Iraw_10_3, VdRaw_10_3, Iraw_10_, VdRaw_10_

Iraw3 = np.array(Iraw3)
Iraw = np.array(Iraw)

Iraw_10_3 = np.array(Iraw_10_3)
Iraw_10_ = np.array(Iraw_10_)

ratios = Iraw / Iraw3
ratios2 = Iraw_10_ / Iraw_10_3


if __name__ == '__main__':

    # Setting up plot
    title = "Ratio of Parallel to Singular Transitor"
    yLabel = "Ratio of Parallel to Singular"
    xLabel = "Gate Voltage (V)"

    # Plotting Data

    Data1 = plt.plot(VdRaw3, ratios, 'ro', markersize=3, label="Vd = Vdd")
    Data1 = plt.plot(VdRaw_10_3, ratios2, 'bo', markersize=3, label="Vd = 10 mV")

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.savefig('parallel_ratios.png', format='png')

    plt.show()
