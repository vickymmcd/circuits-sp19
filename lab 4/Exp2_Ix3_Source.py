

# Simple I-V Graph
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats

# Importing Data
#100 Ohm
I_yTemp = open('exp2/ix3-source/Iy.txt', 'r').read().split()
I_zTemp = open('exp2/ix3-source/Iz.txt', 'r').read().split()

I_y = []
I_z = []

Theo_Z = []

I_x = 1e-3

i = 0
for x in I_yTemp:
    I_yVal = float(x)
    I_zVal = float(I_zTemp[i])
    I_y.append(I_yVal)
    I_z.append(I_zVal)
    print(I_yVal)
    Theo_Z.append(np.sqrt(I_yVal*I_x))

    i = i + 1

# print(math.sqrt(0.000001*I_x))

# Setting up plot
title = "Translinear cirucit output current (Iz) verse input current (Iy)"
yLabel = "Iz (Amps)"
xLabel = "Iy (Amps)"


# Plotting Data

Data1 = plt.loglog(I_z, I_y, 'ro', markersize=3, label="Ix = 1e^-4")
Data2 = plt.loglog(Theo_Z, I_y, 'b--', markersize=3, label="Theoreical")

plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.savefig('Exp2_Ix3_Source.png', format='png')
plt.show()


#
