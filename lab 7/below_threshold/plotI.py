
import numpy as np
import math
import matplotlib.pyplot as plt
from numpy import *

# Importing Data
I1V3Raw = open('v2=3/I1.txt', 'r').read().split() # Drain Currrent I1
I2V3Raw = open('v2=3/I2.txt', 'r').read().split() # Drain Currrent I1
VdmV3Raw = open('v2=3/Vdm.txt', 'r').read().split() # Vdm

I1V4Raw = open('v2=4/I1.txt', 'r').read().split() # Drain Currrent I1
I2V4Raw = open('v2=4/I2.txt', 'r').read().split() # Drain Currrent I1
VdmV4Raw = open('v2=4/Vdm.txt', 'r').read().split() # Vdm

I1V5Raw = open('v2=5/I1.txt', 'r').read().split() # Drain Currrent I1
I2V5Raw = open('v2=5/I2.txt', 'r').read().split() # Drain Currrent I1
VdmV5Raw = open('v2=5/Vdm.txt', 'r').read().split() # Vdm

I1V3 = []
I2V3 = []
Vdm3 = []

I1V4 = []
I2V4 = []
Vdm4 = []

I1V5 = []
I2V5 = []
Vdm5 = []

Diff3 = []
Diff4 = []
Diff5 = []

Sum3 = []
Sum4 = []
Sum5 = []

i = 0
for x in I1V3Raw:
    I1V3.append(float(x))
    Vdm3.append(float(VdmV3Raw[i]))
    I2V3.append(float(I2V3Raw[i]))

    I1V4.append(float(I1V4Raw[i]))
    Vdm4.append(float(VdmV4Raw[i]))
    I2V4.append(float(I2V4Raw[i]))

    I1V5.append(float(I1V5Raw[i]))
    Vdm5.append(float(VdmV5Raw[i]))
    I2V5.append(float(I2V5Raw[i]))

    Diff3.append(float(I1V3Raw[i])-float(I2V3Raw[i]))
    Diff4.append(float(I1V4Raw[i])-float(I2V4Raw[i]))
    Diff5.append(float(I1V5Raw[i])-float(I2V5Raw[i]))

    Sum3.append(float(I1V3Raw[i])+float(I2V3Raw[i]))
    Sum4.append(float(I1V4Raw[i])+float(I2V4Raw[i]))
    Sum5.append(float(I1V5Raw[i])+float(I2V5Raw[i]))

    i+=1



if __name__ == "__main__":
    # Setting up plot
    title = "Current as a function of Vdm"
    yLabel = "Current (I)"
    xLabel = "Voltage Differnce Vdm (V)"

    Data1 = plt.plot(Vdm3, I1V3, 'ro', markersize=3, label="I1, V2 = 3")
    Data2 = plt.plot(Vdm4, I1V4, 'ko', markersize=3, label="I1, V2 = 4")
    Data3 = plt.plot(Vdm5, I1V3, 'bo', markersize=3, label="I1, V2 = 5")

    Data4 = plt.plot(Vdm3, I2V3, 'r*', markersize=3, label="I2, V2 = 3")
    Data5 = plt.plot(Vdm4, I2V4, 'k*', markersize=3, label="I2, V2 = 4")
    Data6 = plt.plot(Vdm5, I2V3, 'b*', markersize=3, label="I2, V2 = 5")

    Data7 = plt.plot(Vdm3, Sum3, 'r--', markersize=3, label="I1 - I2, V2 = 3")
    Data8 = plt.plot(Vdm4, Sum4, 'k--', markersize=3, label="I1 - I2, V2 = 4")
    Data9 = plt.plot(Vdm5, Sum5, 'b--', markersize=3, label="I1 - I2, V2 = 5")

    Data7 = plt.plot(Vdm3, Diff3, 'r^', markersize=3, label="I1 + I2, V2 = 3")
    Data8 = plt.plot(Vdm4, Diff4, 'k^', markersize=3, label="I1 + I2, V2 = 4")
    Data9 = plt.plot(Vdm5, Diff5, 'b^', markersize=3, label="I1 + I2, V2 = 5")

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.savefig('CurrentPlot.png', format='png')
    plt.show()



#
