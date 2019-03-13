

# Simple I-V Graph
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats

# Importing Data
#100 Ohm
I_yTemp = open('exp2/ix1-source/Iy.txt', 'r').read().split()
I_zTemp = open('exp2/ix1-source/Iz.txt', 'r').read().split()

I_y = []
I_z = []

i = 0
for x in I_yTemp:
    I_yVal = float(x)
    I_zVal = float(I_zTemp[i])
    I_y.append(I_yVal)
    I_z.append(I_zVal)
    i = i + 1


# Setting up plot
title = "Translinear cirucit output current (Iz) verse input current (Iy)"
yLabel = "Iz (Amps)"
xLabel = "Iy (Amps)"


# Plotting Data

Data1 = plt.loglog(I_z, I_y, 'ro', markersize=3)

plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.savefig('Exp2_Ix1_Source.png', format='png')
plt.show()


#
