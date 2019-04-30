import numpy as np
import math
import matplotlib.pyplot as plt
from numpy import *
from scipy import stats

# # Importing Data
# I1V3Raw = open('v2=3/I1.txt', 'r').read().split() # Drain Currrent I1
# I2V3Raw = open('v2=3/I2.txt', 'r').read().split() # Drain Currrent I1
# VdmV3Raw = open('v2=3/Vdm.txt', 'r').read().split() # Vdm

VoutRaw = open('first/Vout.txt', 'r').read().split()
VInRaw = open('first/V1.txt', 'r').read().split()


#
# I1V4Raw = open('v2=4/I1.txt', 'r').read().split() # Drain Currrent I1
# I2V4Raw = open('v2=4/I2.txt', 'r').read().split() # Drain Currrent I1
# VdmV4Raw = open('v2=4/Vdm.txt', 'r').read().split() # Vdm
#
# I1V5Raw = open('v2=5/I1.txt', 'r').read().split() # Drain Currrent I1
# I2V5Raw = open('v2=5/I2.txt', 'r').read().split() # Drain Currrent I1
# VdmV5Raw = open('v2=5/Vdm.txt', 'r').read().split() # Vdm

Vout = []
VIn = []



BestFitLine = []
i = 0
for x in VoutRaw:
    Vout.append(float(x))
    VIn.append(float(VInRaw[i]))
    i+=1

NumVout = np.array(Vout)
NumVIn = np.array(VIn)

slope, intercept, r_value, p_value, std_err = stats.linregress(NumVIn, NumVout)
line = slope*NumVIn+intercept
print(slope)

if __name__ == "__main__":
    # Setting up plot
    title = "VTC of Unity-Gain Follower"
    yLabel = "Vout (V)"
    xLabel = "Vin (V)"


    Data1 = plt.plot(NumVIn, NumVout, 'ro', markersize=3, label="VTC")
    Data2 = plt.plot(NumVIn, line, 'ko', markersize=3, label="Best Fit Line")

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.savefig('VTC.png', format='png')
    plt.show()



#
