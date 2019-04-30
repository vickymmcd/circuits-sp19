
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import stats
from numpy import *

# Importing Data
Iout = open('finallyx3/Iout.txt', 'r').read().split() # Iout

Vdm = open('finallyx3/Vdm.txt', 'r').read().split() # Vdm

lineariout = []
linearvdm = []

for i, x in enumerate(Iout):
    Iout[i] = -1*float(Iout[i])*1e6
    Vdm[i] = float(Vdm[i])
    if Vdm[i] > -.045 and Vdm[i] < .03:
        lineariout.append(Iout[i])
        linearvdm.append(Vdm[i])

slope, intercept, r_value, p_value, std_err = stats.linregress(linearvdm, lineariout)
linearvdm = np.array(linearvdm)

# resistance = slope / 1000000
# resistance = 1/resistance
# print(resistance)


if __name__ == "__main__":
    # Setting up plot
    title = "Current as a function of Vdm"
    yLabel = "Iout (micro amps)"
    xLabel = "Vdm (V)"

    Data1 = plt.plot(Vdm, Iout, 'ro', markersize=3, label="Vout=3.35V")
    Data = plt.plot(linearvdm, (slope*linearvdm)+intercept, 'b', label="best fit line: y="+str(round(slope,5))+"x + " +str(round(intercept,5)))

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.savefig('exp2_transconductance.png', format='png')
    plt.show()
