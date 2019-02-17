
# Simple I-V Graph


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

Vin = open('exp 2 110 resistor/Vin.txt', 'r').read().split()
I100 = open('exp 2 110 resistor/I.txt', 'r').read().split()

linear_i = []
linear_v = []


i = 0
for x in Vin:
    val = float(x)
    Vin[i]= val
    i = i+1

i = 0
for x in I100:
    val = float(x)
    I100[i]= val
    if Vin[i] > .5:
        linear_i.append(val)
        linear_v.append(Vin[i])
    i = i+1

title = "Plot of Voltage Vs Current"
xLabel = "Voltage In (V)"
yLabel = "Current Out (A)"

slope, intercept, r_value, p_value, std_err = stats.linregress(linear_v, linear_i)
linear_v = np.array(linear_v)

von100 = (-1*intercept)/slope

if __name__ == '__main__':
    title = "Plot of Voltage Vs Current"
    xLabel = "Voltage In (V)"
    yLabel = "Current Out (A)"
    linear_v = np.array(linear_v)
    Vin = np.array(Vin)

    Data = plt.plot(Vin, I100, 'bo', markersize=3, label="110 Ohm Resistor")
    Data = plt.plot(Vin, (slope*Vin)+intercept, 'r', label="fitted line: y="+str(round(slope,5))+"x + " +str(round(intercept,5)))


    plt.legend()
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.grid(True)
    plt.show()
