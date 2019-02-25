
# Simple I-V Graph


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

Vb = open('exp3-100/Vb.txt', 'r').read().split()
Vout = open('exp3-100/Vout.txt', 'r').read().split()


i = 0
for x in Vb:
    val = float(x)
    Vb[i]= val
    i = i+1

i = 0
for x in Vout:
    val = float(x)
    Vout[i]= val
    i = i+1

slope, intercept, r_value, p_value, std_err = stats.linregress(Vb, Vout)
Vb = np.array(Vb)



if __name__ == '__main__':
    title = "Plot of Voltage Transfer Characteristic"
    xLabel = "Voltage In (V)"
    yLabel = "Voltage Out (V)"

    Data = plt.plot(Vb, Vout, 'bo', markersize=3, label="100 Ohm Resistor")
    Data = plt.plot(Vb, (slope*Vb)+intercept, 'r', label="fitted line: y="+str(round(slope,5))+"x + " +str(round(intercept,5)))


    plt.legend()
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.grid(True)
    plt.show()
