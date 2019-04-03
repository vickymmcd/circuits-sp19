# -*- coding: utf-8 -*-

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Importing Data
Iraw = open('parallel/5V/Id.txt', 'r').read().split()
VdRaw = open('parallel/5V/Vg.txt', 'r').read().split()
Iraw2 = open('series/5V/Id.txt', 'r').read().split()
VdRaw2 = open('series/5V/Vg.txt', 'r').read().split()
Iraw3 = open('singular/5V/Id.txt', 'r').read().split()
VdRaw3 = open('singular/5V/Vg.txt', 'r').read().split()


i = 0
for x in Iraw:
    Iraw[i] = float(Iraw[i])
    VdRaw[i] = float(VdRaw[i])
    i+=1


i = 0
for x in Iraw2:
    Iraw2[i] = float(Iraw2[i])
    VdRaw2[i] = float(VdRaw2[i])
    i+=1

i = 0
for x in Iraw3:
    Iraw3[i] = float(Iraw3[i])
    VdRaw3[i] = float(VdRaw3[i])
    i+=1


if __name__ == '__main__':

    # Setting up plot
    title = "Series and Parallel Transistors with Vd=Vdd"
    yLabel = "Channel Current (A)"
    xLabel = "Gate Voltage (V)"

    # Plotting Data

    Data1 = plt.semilogy(VdRaw, Iraw, 'ro', markersize=3, label="Parallel")
    Data1 = plt.semilogy(VdRaw2, Iraw2, 'go', markersize=3, label="Series")
    Data1 = plt.semilogy(VdRaw3, Iraw3, 'bo', markersize=3, label="Singular")

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.savefig('exp2vdd.png', format='png')

    plt.show()
