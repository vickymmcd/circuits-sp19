
#Sweeping Ix, setting Iy

# Simple I-V Graph
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats

# Importing Data
#100 Ohm
I_x1Temp = open('exp2/294k-sink/Ix.txt', 'r').read().split()
I_z1Temp = open('exp2/294k-sink/Iz.txt', 'r').read().split()

I_x2Temp = open('exp2/28k-sink/Ix.txt', 'r').read().split()
I_z2Temp = open('exp2/28k-sink/Iz.txt', 'r').read().split()

I_x3Temp = open('exp2/2.94k-sink/Ix.txt', 'r').read().split()
I_z3Temp = open('exp2/2.94k-sink/Iz.txt', 'r').read().split()

I_x1 = []
I_z1 = []

I_x2 = []
I_z2 = []

I_x3 = []
I_z3 = []

Theo_Z1 = []
Theo_Z2 = []
Theo_Z3 = []

I_y1 = 0.000001

i = 0
for x in I_x1Temp:
    I_xVal = float(x)
    I_zVal = -1*float(I_z1Temp[i])
    I_x1.append(I_xVal)
    I_z1.append(I_zVal)
    Theo_Z1.append(np.sqrt(I_xVal*I_y1))

    i = i + 1

I_y2 = 0.00001

i = 0
for x in I_x2Temp:
    I_xVal = float(x)
    I_zVal = -1*float(I_z2Temp[i])
    I_x2.append(I_xVal)
    I_z2.append(I_zVal)
    Theo_Z2.append(np.sqrt(I_xVal*I_y2))
    i = i + 1

I_y3 = 0.0001

i = 0
for x in I_x3Temp:
    I_xVal = float(x)
    I_zVal = -1*float(I_z3Temp[i])
    I_x3.append(I_xVal)
    I_z3.append(I_zVal)
    Theo_Z3.append(np.sqrt(I_xVal*I_y3))
    i = i + 1

# print(math.sqrt(0.000001*I_x))

# Setting up plot
title = "Translinear cirucit output current (Iz) verse input current (Ix)"
yLabel = "Iz (A)"
xLabel = "Ix (A)"

# Plotting Data

Data1 = plt.loglog(I_z1, I_x1, 'ro', markersize=3, label="Iy = 1e^-6")
Data2 = plt.loglog(Theo_Z1, I_x1, 'r--', markersize=3, label="Iz = 1e^-6 *Iy")
Data3 = plt.loglog(I_z2, I_x2, 'go', markersize=3, label="Iy = 1e^-5")
Data4 = plt.loglog(Theo_Z2, I_x2, 'g--', markersize=3, label="Iz = 1e^-5 *Iy")
Data5 = plt.loglog(I_z3, I_x3, 'bo', markersize=3, label="Iy = 1e^-4")
Data6 = plt.loglog(Theo_Z3, I_x3, 'b--', markersize=3, label="Iz = 1e^-4 *Iy")

plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.legend()
plt.savefig('Exp2_Sink.png', format='png')
plt.show()


#
