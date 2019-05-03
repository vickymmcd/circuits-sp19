
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

BestFitLine = []

i = 0
I1Shift = 20

for x in I1V3Raw:
    if(i>I1Shift):
        I1V3.append(float(x))
    I2V3.append(float(I2V3Raw[i]))
    Vdm3.append(float(VdmV3Raw[i]))

    I1V4.append(float(I1V4Raw[i]))
    Vdm4.append(float(VdmV4Raw[i]))
    I2V4.append(float(I2V4Raw[i]))

    I1V5.append(float(I1V5Raw[i]))
    Vdm5.append(float(VdmV5Raw[i]))
    I2V5.append(float(I2V5Raw[i]))
    if(i>I1Shift):
        Diff3.append(float(I1V3Raw[i])-float(I2V3Raw[i]))
    Diff4.append(float(I1V4Raw[i])-float(I2V4Raw[i]))
    Diff5.append(float(I1V5Raw[i])-float(I2V5Raw[i]))

    if(i>I1Shift):
        Sum3.append(float(I1V3Raw[i])+float(I2V3Raw[i]))
    Sum4.append(float(I1V4Raw[i])+float(I2V4Raw[i]))
    Sum5.append(float(I1V5Raw[i])+float(I2V5Raw[i]))

    i+=1


gDM3Diff = np.diff(Vdm3)
I3DiffRaw = np.diff(Diff3)
I3Diff = []

gDM4Diff = np.diff(Vdm4)
I4DiffRaw = np.diff(Diff4)
I4Diff = []


gDM5Diff = np.diff(Vdm5)
I5DiffRaw = np.diff(Diff5)
I5Diff = []

I1lastVal = I1V3[i-I1Shift-2]

for m in I3DiffRaw:
    I3Diff.append(m)

for m in I4DiffRaw:
    I4Diff.append(m)

for m in I5DiffRaw:
    I5Diff.append(m)

for x in range(0,I1Shift+1):
    I1V3.append(None)
    Diff3.append(None)
    Sum3.append(None)
    # I3Diff.append(0)

gmn3 = []
line3 = []

gmn4 = []
line4 = []

gmn5 = []
line5 = []

for n in I3Diff:
    gmn3.append(n/gDM3Diff[0])

for n in I4Diff:
    gmn4.append(n/gDM4Diff[0])

for n in I5Diff:
    gmn5.append(n/gDM5Diff[0])

slope3 = gmn3[round(len(gmn3)/2)]

slope4 = gmn4[round(len(gmn4)/2)]

slope5 = gmn5[round(len(gmn5)/2)]

print(slope3)
print(slope4)
print(slope5)

print("Sum three", Sum3)
print("Sum four", Sum4)

for xx in Vdm4:
    line3.append(xx*slope3)
    line4.append(xx*slope4)
    line5.append(xx*slope5)

if __name__ == "__main__":
    # Setting up plot
    title = "Current as a function of Vdm Below Threshold"
    yLabel = "Current (A)"
    xLabel = "Voltage Differnce Vdm (V)"


    Data1 = plt.plot(Vdm4, I1V3, 'ro', markersize=3, label="I1, V2 = 3V")
    Data2 = plt.plot(Vdm4, I1V4, 'ko', markersize=3, label="I1, V2 = 4V")
    Data3 = plt.plot(Vdm5, I1V5, 'bo', markersize=3, label="I1, V2 = 5V")



    Data4 = plt.plot(Vdm3, I2V3, 'r*', markersize=3, label="I2, V2 = 3V")
    Data5 = plt.plot(Vdm4, I2V4, 'k*', markersize=3, label="I2, V2 = 4V")
    Data6 = plt.plot(Vdm5, I2V5, 'b*', markersize=3, label="I2, V2 = 5V")

    Data7 = plt.plot(Vdm3, Sum3, 'r--', markersize=3, label="I1 - I2, V2 = 3V")
    Data8 = plt.plot(Vdm4, Sum4, 'k--', markersize=3, label="I1 - I2, V2 = 4V")
    Data9 = plt.plot(Vdm5, Sum5, 'b--', markersize=3, label="I1 - I2, V2 = 5V")

    Data7 = plt.plot(Vdm3, Diff3, 'r^', markersize=3, label="I1 + I2, V2 = 3V")
    Data8 = plt.plot(Vdm4, Diff4, 'k^', markersize=3, label="I1 + I2, V2 = 4V")
    Data9 = plt.plot(Vdm5, Diff5, 'b^', markersize=3, label="I1 + I2, V2 = 5V")

    mOffset = 18;
    Date10 = plt.plot(Vdm4[mOffset:len(line3)-mOffset], line3[mOffset:len(line3)-mOffset], 'c',  markersize=3, label="slope = Gdm, V2=3V")
    Date11 = plt.plot(Vdm4[mOffset:len(line3)-mOffset], line4[mOffset:len(line4)-mOffset], 'g',  markersize=3, label="slope = Gdm, V2=4V")
    Date12 = plt.plot(Vdm4[mOffset:len(line3)-mOffset], line5[mOffset:len(line5)-mOffset], 'm',  markersize=3, label="slope = Gdm, V2=5V")

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.savefig('CurrentPlot.png', format='png')
    plt.show()



#
