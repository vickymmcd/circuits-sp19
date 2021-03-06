
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import stats
from numpy import *

# Importing Data
Iout = open('vdm=0x2/Iout.txt', 'r').read().split() # Iout

Vout = open('vdm=0x2/Vout.txt', 'r').read().split() # Vout

lineariout = []
linearvout = []

for i, x in enumerate(Iout):
    Iout[i] = float(Iout[i])*1e6
    Vout[i] = float(Vout[i])
    if Vout[i] > 1.16 and Vout[i] < 4.9:
        lineariout.append(Iout[i])
        linearvout.append(Vout[i])

slope, intercept, r_value, p_value, std_err = stats.linregress(linearvout, lineariout)
linearvout = np.array(linearvout)

resistance = slope / 1000000
print(1/slope)
resistance = 1/resistance
print(resistance)


if __name__ == "__main__":
    # Setting up plot
    title = "Current Voltage Characteristic"
    yLabel = "Iout (micro amps)"
    xLabel = "Vout (V)"

    Data1 = plt.plot(Vout, Iout, 'ro', markersize=3)
    Data = plt.plot(linearvout, (slope*linearvout)+intercept, 'b', label="best fit line: y="+str(round(slope,5))+"x + " +str(round(intercept,5)))

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.savefig('exp2_resistance.png', format='png')
    plt.show()
