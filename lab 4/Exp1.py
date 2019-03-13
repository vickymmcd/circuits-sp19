

# Simple I-V Graph
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats

# Importing Data
#100 Ohm
Ib1 = open('exp1/1/Ib.txt', 'r').read().split()
Ie1 = open('exp1/1/Ie.txt', 'r').read().split()
Bb1 = open('exp1/1/Vb.txt', 'r').read().split()

Ib2 = open('exp1/2/Ib.txt', 'r').read().split()
Ie2 = open('exp1/2/Ie.txt', 'r').read().split()
Bb2 = open('exp1/2/Vb.txt', 'r').read().split()

Ib3 = open('exp1/3/Ib.txt', 'r').read().split()
Ie3 = open('exp1/3/Ie.txt', 'r').read().split()
Bb3 = open('exp1/3/Vb.txt', 'r').read().split()

Ib4 = open('exp1/4/Ib.txt', 'r').read().split()
Ie4 = open('exp1/4/Ie.txt', 'r').read().split()
Bb4 = open('exp1/4/Vb.txt', 'r').read().split()

I_b1 = []
I_z1 = []
V_1 = []

I_b2 = []
I_z2 = []

I_b3 = []
I_z3 = []

I_b4 = []
I_z4 = []



i = 0
for x in Ib1:
    IbVal = float(x)
    I_zVal = (Ie1[i])
    I_z1.append(I_zVal)
    I_b1.append(IbVal)
    V_1.append(float(Bb1[i]))


    i = i + 1



i = 0
for x in Ib2:
    IbVal = float(x)
    I_zVal = (Ie2[i])
    I_z2.append(I_zVal)
    I_b2.append(IbVal)

    i = i + 1
i = 0
for x in Ib3:
    IbVal = float(x)
    I_zVal = (Ie3[i])
    I_z3.append(I_zVal)
    I_b3.append(IbVal)

    i = i + 1

i = 0

for x in Ib4:
    IbVal = float(x)
    I_zVal = (Ie4[i])
    I_z4.append(I_zVal)
    I_b4.append(IbVal)

    i = i + 1

# print(math.sqrt(0.000001*I_x))

# Setting up plot
title = "Translinear cirucit output current (Iz) verse input current (Iy)"
yLabel = "Ie (A)"
xLabel = "Ib (A)"

# Plotting Data

Data1 = plt.plot(V_1, I_z1, 'ro', markersize=3)
# Data1 = plt.loglog(I_b2, I_z2, 'go', markersize=3)
# Data1 = plt.loglog(I_b3, I_z3, 'bo', markersize=3)
# Data1 = plt.loglog(I_b4, I_z4, 'r--', markersize=3)

plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.legend()
plt.savefig('Exp2_Ix3_Source.png', format='png')
plt.show()


#
