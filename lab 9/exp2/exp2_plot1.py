
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import stats
from numpy import *

# Importing Data
Vdm = open('gain/Vdm.txt', 'r').read().split() # Vdm

Vout = open('gain/Vout.txt', 'r').read().split() # Vout

linearvdm = []
linearvout = []

for i, x in enumerate(Vdm):
    Vdm[i] = float(Vdm[i])
    Vout[i] = float(Vout[i])
    if Vdm[i] > -.0007 and Vdm[i] < .02:
        linearvdm.append(Vdm[i])
        linearvout.append(Vout[i])


slope, intercept, r_value, p_value, std_err = stats.linregress(linearvdm, linearvout)
linearvdm = np.array(linearvdm)


if __name__ == "__main__":
    # Setting up plot
    title = "Vout as a function of Vdm"
    yLabel = "Vout (V)"
    xLabel = "Voltage Differnce Vdm (V)"

    Data1 = plt.plot(Vdm, Vout, 'ro', markersize=3, label="V2 = 3V")
    Data = plt.plot(linearvdm, (slope*linearvdm)+intercept, 'b', label="best fit line: y="+str(round(slope,5))+"x + " +str(round(intercept,5)))

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.savefig('exp2_gain.png', format='png')
    plt.show()
