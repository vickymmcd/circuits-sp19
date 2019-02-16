
# Simple I-V Graph


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

Vin = open('exp 2 1100 resistor/Vin.txt', 'r').read().split()
I1K = open('exp 2 1100 resistor/I.txt', 'r').read().split()

linear_i = []
linear_v = []


i = 0
for x in Vin:
    val = float(x)
    Vin[i]= val
    i = i+1

i = 0
for x in I1K:
    val = float(x)
    I1K[i]= val
    if Vin[i] > .5:
        linear_i.append(val)
        linear_v.append(Vin[i])
    i = i+1

slope, intercept, r_value, p_value, std_err = stats.linregress(linear_v, linear_i)
linear_v = np.array(linear_v)

von1k = (-1*intercept)/slope

print(von1k)


title = "Plot of Voltage Vs Current"
xLabel = "Voltage In (V)"
yLabel = "Current Out (A)"
linear_v = np.array(linear_v)
Vin = np.array(Vin)

Data = plt.plot(Vin, I1K, 'bo', markersize=3, label="1100 Ohm Resistor")
Data = plt.plot(Vin, (slope*Vin)+intercept, 'r', label="fitted line: y="+str(round(slope,5))+"x + " +str(round(intercept,5)))


plt.legend()
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.grid(True)
plt.show()
