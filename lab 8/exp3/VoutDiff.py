import numpy as np
import math
import matplotlib.pyplot as plt
from numpy import *
from scipy import stats

# # Importing Data
# I1V3Raw = open('v2=3/I1.txt', 'r').read().split() # Drain Currrent I1
# I2V3Raw = open('v2=3/I2.txt', 'r').read().split() # Drain Currrent I1
# VdmV3Raw = open('v2=3/Vdm.txt', 'r').read().split() # Vdm

VoutDiffRaw = open('secondvout-vin/Vout.txt', 'r').read().split()
VInRaw = open('secondvout-vin/V1.txt', 'r').read().split()


VoutDiff = []
VIn = []

i = 0
for x in VoutDiffRaw:
    VoutDiff.append(float(x))
    VIn.append(float(VInRaw[i]))
    i+=1

if __name__ == "__main__":
    # Setting up plot
    title = "Vout-Vin of Unity-Gain Follower"
    yLabel = "Vout (V)"
    xLabel = "Vin (V)"


    Data1 = plt.plot(VIn, VoutDiff, 'ro', markersize=3, label="Vout-Vin")

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.savefig('VTCDiff.png', format='png')
    plt.show()



#
