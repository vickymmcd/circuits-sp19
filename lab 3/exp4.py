
# Simple I-V Graph


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from exp3 import Von

Vb = open('exp4-300/Vin.txt', 'r').read().split()
Vout = open('exp4-300/Vout.txt', 'r').read().split()
Vout2 = open('exp4-400/Vout.txt', 'r').read().split()
Vout3 = open('exp4-500/Vout.txt', 'r').read().split()
downwardVin, downwardVin2, downwardVin3 = [], [], []
downwardVout, downwardVout2, downwardVout3 = [], [], []


i = 0
for x in Vb:
    val = float(x)
    Vb[i]= val
    i = i+1

i = 0
for x in Vout:
    val = float(x)
    Vout[i]= val
    if Vb[i] > 1 and Vb[i] < 2:
        downwardVout.append(val)
        downwardVin.append(Vb[i])
    i = i+1

i = 0
for x in Vout2:
    val = float(x)
    Vout2[i]= val
    if Vb[i] > 1 and Vb[i] < 1.8:
        downwardVout2.append(val)
        downwardVin2.append(Vb[i])
    i = i+1

i = 0
for x in Vout3:
    val = float(x)
    Vout3[i]= val
    if Vb[i] > 1 and Vb[i] < 1.7:
        downwardVout3.append(val)
        downwardVin3.append(Vb[i])
    i = i+1

slope, intercept, r_value, p_value, std_err = stats.linregress(downwardVin, downwardVout)
slope2, intercept2, r_value, p_value, std_err = stats.linregress(downwardVin2, downwardVout2)
slope3, intercept3, r_value, p_value, std_err = stats.linregress(downwardVin3, downwardVout3)

downwardVin = np.array(downwardVin)
downwardVin2 = np.array(downwardVin2)
downwardVin3 = np.array(downwardVin3)



if __name__ == '__main__':
    title = "Plot of Voltage Transfer Characteristic"
    xLabel = "Voltage In (V)"
    yLabel = "Voltage Out (V)"

    Data = plt.plot(Vb, Vout, 'bo', markersize=3, label="300 Ohm Resistor")
    Data = plt.plot(Vb, Vout2, 'ro', markersize=3, label="400 Ohm Resistor")
    Data = plt.plot(Vb, Vout3, 'go', markersize=3, label="500 Ohm Resistor")
    Data = plt.plot(downwardVin, (slope*downwardVin)+intercept, 'b', markersize=3, label="300 Ohm Resistor Theoretical: y="+str(round(slope,5))+"x + " +str(round(intercept,5)))
    Data = plt.plot(downwardVin2, (slope2*downwardVin2)+intercept2, 'r', markersize=3, label="400 Ohm Resistor Theoretical: y="+str(round(slope2,5))+"x + " +str(round(intercept2,5)))
    Data = plt.plot(downwardVin3, (slope3*downwardVin3)+intercept3, 'g', markersize=3, label="500 Ohm Resistor Theoretical: y="+str(round(slope3,5))+"x + " +str(round(intercept3,5)))

    Data = plt.plot(Vb, (1*Vb)+(-1*Von), 'k', label="theoretical: y="+str(round(1,5))+"x + " +str(round((-1*Von),5)))


    plt.legend()
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.grid(True)
    plt.show()
