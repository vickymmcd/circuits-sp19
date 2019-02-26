
# Simple I-V Graph


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from ExpConstantCalcs import U_t, I_s

Vb = open('exp3-100/Vin.txt', 'r').read().split()
Vout = open('exp3-100/Vout.txt', 'r').read().split()
beta = 100
Ut = U_t #.033
Is = I_s #1*10**-13
R = 100
alpha = float(beta/(1.0+beta))
Ion = (alpha*Ut)/R
Von = Ut*np.log(Ion/Is)


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

# slope, intercept, r_value, p_value, std_err = stats.linregress(Vb, Vout)
Vb = np.array(Vb)
slope = 1
intercept = -1*Von



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
