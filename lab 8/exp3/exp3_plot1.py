
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import stats
from numpy import *

# Importing Data
Vdm = open('first/V1.txt', 'r').read().split() # Vdm

Vout = open('first/Vout.txt', 'r').read().split() # Vout

linearvdm = []
linearvout = []

for i, x in enumerate(Vdm):
    Vdm[i] = float(Vdm[i])
    Vout[i] = float(Vout[i])
    if Vdm[i] > .5 and Vdm[i] < 4:
        linearvdm.append(Vdm[i])
        linearvout.append(Vout[i])


slope, intercept, r_value, p_value, std_err = stats.linregress(linearvdm, linearvout)
linearvdm = np.array(linearvdm)


if __name__ == "__main__":
    # Setting up plot
    title = "VTC of Unity-Gain Follower"
    yLabel = "Vout (V)"
    xLabel = "V1 (V)"

    Data1 = plt.plot(Vdm, Vout, 'ro', markersize=3, label="VTC")
    Data = plt.plot(linearvdm, (slope*linearvdm)+intercept, 'b', label="best fit line: y="+str(round(slope,5))+"x + " +str(round(intercept,5)))

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.savefig('VTC2.png', format='png')
    plt.show()
