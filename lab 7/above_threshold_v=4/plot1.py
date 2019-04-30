
import numpy as np
import math
import matplotlib.pyplot as plt
from numpy import *


I1V4Raw = open('I1.txt', 'r').read().split() # Drain Currrent I1
I2V4Raw = open('I2.txt', 'r').read().split() # Drain Currrent I1
VdmV4Raw = open('Vdm.txt', 'r').read().split() # Vdm

I1V4 = []
I2V4 = []
Vdm4 = []

Diff4 = []
Sum4 = []

BestFitLine = []
i = 0
for x in I1V4Raw:
    I1V4.append(float(x))
    Vdm4.append(float(VdmV4Raw[i]))
    I2V4.append(float(I2V4Raw[i]))

    Diff4.append(float(I1V4Raw[i])-float(I2V4Raw[i]))

    Sum4.append(float(I1V4Raw[i])+float(I2V4Raw[i]))
    i+=1


gDM4Diff = np.diff(Vdm4)
I4DiffRaw = np.diff(Diff4)
I4Diff = []

for m in I4DiffRaw:
    I4Diff.append(m)

gmn4 = []
line4 = []

for n in I4Diff:
    gmn4.append(n/gDM4Diff[0])


slope4 = gmn4[round(len(gmn4)/2)]
print(slope4)

for xx in Vdm4:
    line4.append(xx*slope4)

if __name__ == "__main__":
    # Setting up plot
    title = "Current as a function of Vdm Above Threshold"
    yLabel = "Current (I)"
    xLabel = "Voltage Differnce Vdm (V)"


    Data2 = plt.plot(Vdm4, I1V4, 'bo', markersize=3, label="I1, V2 = 4V")

    Data5 = plt.plot(Vdm4, I2V4, 'ko', markersize=3, label="I2, V2 = 4V")

    Data8 = plt.plot(Vdm4, Sum4, 'ro', markersize=3, label="I1 - I2, V2 = 4V")

    Data9 = plt.plot(Vdm4, Diff4, 'co', markersize=3, label="I1 + I2, V2 = 4V")

    mOffset = 10;
    Date11 = plt.plot(Vdm4[mOffset:len(line4)-mOffset], line4[mOffset:len(line4)-mOffset], 'g',  markersize=3, label="slope = Gdm, V2=4V")

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.savefig('CurrentPlotAbove.png', format='png')
    plt.show()



#
