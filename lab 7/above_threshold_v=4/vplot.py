
import numpy as np
import math
import matplotlib.pyplot as plt
from numpy import *

# Importing Data
VdmRaw = open('Vdm.txt', 'r').read().split() # Vdm

VV4Raw = open('V.txt', 'r').read().split() # common source node voltage


i = 0
for x in VV4Raw:
    VV4Raw[i] = float(VV4Raw[i])
    VdmRaw[i] = float(VdmRaw[i])

    i+=1



if __name__ == "__main__":
    # Setting up plot
    title = "Voltage as a function of Vdm"
    yLabel = "Voltage (V)"
    xLabel = "Voltage Differnce Vdm (V)"

    Data2 = plt.plot(VdmRaw, VV4Raw, 'go', markersize=3, label="V2 = 4")

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.savefig('VoltagePlotAbove.png', format='png')
    plt.show()



#
