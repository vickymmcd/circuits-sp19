

# Simple I-V Graph
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats

# Importing Data
#100 Ohm
I_y1Temp = open('exp22/294k-sink/Ix.txt', 'r').read().split()
I_z1Temp = open('exp22/294k-sink/Iz.txt', 'r').read().split()

I_y2Temp = open('exp22/28.0k-sink/Ix.txt', 'r').read().split()
I_z2Temp = open('exp22/28.0k-sink/Iz.txt', 'r').read().split()

I_y3Temp = open('exp22/2.94k-sink/Ix.txt', 'r').read().split()
I_z3Temp = open('exp22/2.94k-sink/Iz.txt', 'r').read().split()

I_y1 = []
I_z1 = []

I_y2 = []
I_z2 = []

I_y3 = []
I_z3 = []

Theo_Z1 = []
Theo_Z2 = []
Theo_Z3 = []

I_x1 = 0.000001

i = 0
for x in I_y1Temp:
    I_yVal = float(x)
    I_zVal = -1*float(I_z1Temp[i])
    I_y1.append(I_yVal)
    I_z1.append(I_zVal)
    Theo_Z1.append(np.sqrt(I_yVal*I_x1))

    i = i + 1

I_x2 = 0.00001

i = 0
for x in I_y2Temp:
    I_yVal = float(x)
    I_zVal = -1*float(I_z2Temp[i])
    I_y2.append(I_yVal)
    I_z2.append(I_zVal)
    Theo_Z2.append(np.sqrt(I_yVal*I_x2))
    i = i + 1

I_x3 = 0.0001
i = 0
for x in I_y3Temp:
    I_yVal = float(x)
    I_zVal = -1*float(I_z3Temp[i])
    I_y3.append(I_yVal)
    I_z3.append(I_zVal)
    Theo_Z3.append(np.sqrt(I_yVal*I_x3))
    i = i + 1

# print(math.sqrt(0.000001*I_x))

# Setting up plot
title = "Translinear cirucit output current (Iz) verse input current (Iy)"
yLabel = "Iz (A)"
xLabel = "Iy (A)"

# Plotting Data

Data1 = plt.loglog(I_z1, I_y1, 'ro', markersize=3, label="Ix = 1e^-6")
Data2 = plt.loglog(Theo_Z1, I_y1, 'r--', markersize=3, label="Theoreical 1e^-6")
Data3 = plt.loglog(I_z2, I_y2, 'go', markersize=3, label="Ix = 1e^-5")
Data4 = plt.loglog(Theo_Z2, I_y2, 'g--', markersize=3, label="Theoreical 1e^-5")
Data5 = plt.loglog(I_z3, I_y3, 'bo', markersize=3, label="Ix = 1e^-4")
Data6 = plt.loglog(Theo_Z3, I_y3, 'b--', markersize=3, label="Theoreical 1e^-4")

plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.legend()
plt.savefig('Exp2_Ix3_Source.png', format='png')
plt.show()


#
