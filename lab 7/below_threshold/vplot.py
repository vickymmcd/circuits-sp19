
import numpy as np
import math
import matplotlib.pyplot as plt
from numpy import *

# Importing Data
VdmRaw = open('v2=3/Vdm.txt', 'r').read().split() # Vdm

VV3Raw = open('v2=3/V.txt', 'r').read().split() # common source node voltage

VV4Raw = open('v2=4/V.txt', 'r').read().split() # common source node voltage

VV5Raw = open('v2=5/V.txt', 'r').read().split() # common source node voltage

i = 0
for x in VV3Raw:
    VV3Raw[i] = float(VV3Raw[i])
    VV4Raw[i] = float(VV4Raw[i])
    VV5Raw[i] = float(VV5Raw[i])
    VdmRaw[i] = float(VdmRaw[i])

    i+=1



if __name__ == "__main__":
    # Setting up plot
    title = "Voltage as a function of Vdm"
    yLabel = "Voltage (V)"
    xLabel = "Voltage Differnce Vdm (V)"

    Data1 = plt.plot(VdmRaw, VV3Raw, 'ro', markersize=3, label="V2 = 3")
    Data2 = plt.plot(VdmRaw, VV4Raw, 'go', markersize=3, label="V2 = 4")
    Data3 = plt.plot(VdmRaw, VV5Raw, 'bo', markersize=3, label="V2 = 5")

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.savefig('VoltagePlot.png', format='png')
    plt.show()



#
