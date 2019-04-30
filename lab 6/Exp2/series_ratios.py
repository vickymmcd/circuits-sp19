# -*- coding: utf-8 -*-

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from exp2vdd import Iraw2, VdRaw2, Iraw3, VdRaw3
from exp2_10mv import Iraw_10_2, VdRaw_10_2, Iraw_10_3, VdRaw_10_3

Iraw2 = np.array(Iraw2)
Iraw3 = np.array(Iraw3)

Iraw_10_2 = np.array(Iraw_10_2)
Iraw_10_3 = np.array(Iraw_10_3)

ratios = Iraw2 / Iraw3
ratios2 = Iraw_10_2 / Iraw_10_3



if __name__ == '__main__':

    # Setting up plot
    title = "Ratio of Series to Singular Transitor"
    yLabel = "Ratio of Series to Singular"
    xLabel = "Gate Voltage (V)"

    # Plotting Data

    Data1 = plt.plot(VdRaw2, ratios, 'ro', markersize=3, label="Vd = Vdd")
    Data1 = plt.plot(VdRaw_10_2, ratios2, 'bo', markersize=3, label="Vd = 10 mV")

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.savefig('series_ratios.png', format='png')

    plt.show()
