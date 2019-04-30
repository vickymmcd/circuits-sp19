# -*- coding: utf-8 -*-

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Importing Data
Iraw_10_ = open('parallel/10mV/Id.txt', 'r').read().split()
VdRaw_10_ = open('parallel/10mV/Vg.txt', 'r').read().split()
Iraw_10_2 = open('series/10mV/Id.txt', 'r').read().split()
VdRaw_10_2 = open('series/10mV/Vg.txt', 'r').read().split()
Iraw_10_3 = open('singular/10mV/Id.txt', 'r').read().split()
VdRaw_10_3 = open('singular/10mV/Vg.txt', 'r').read().split()


i = 0
for x in Iraw_10_:
    Iraw_10_[i] = float(Iraw_10_[i])
    VdRaw_10_[i] = float(VdRaw_10_[i])
    i+=1


i = 0
for x in Iraw_10_2:
    Iraw_10_2[i] = float(Iraw_10_2[i])
    VdRaw_10_2[i] = float(VdRaw_10_2[i])
    i+=1

i = 0
for x in Iraw_10_3:
    Iraw_10_3[i] = float(Iraw_10_3[i])
    VdRaw_10_3[i] = float(VdRaw_10_3[i])
    i+=1


if __name__ == '__main__':

    # Setting up plot
    title = "Series and Parallel Transistors with Vd=10 mV"
    yLabel = "Channel Current (A)"
    xLabel = "Gate Voltage (V)"

    # Plotting Data

    Data1 = plt.semilogy(VdRaw_10_, Iraw_10_, 'ro', markersize=3, label="Parallel")
    Data1 = plt.semilogy(VdRaw_10_2, Iraw_10_2, 'go', markersize=3, label="Series")
    Data1 = plt.semilogy(VdRaw_10_3, Iraw_10_3, 'bo', markersize=3, label="Singular")

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.savefig('exp2_10mv.png', format='png')

    plt.show()
