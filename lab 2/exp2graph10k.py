
# Simple I-V Graph


import numpy as np
import matplotlib.pyplot as plt
from exp2graphall import von10k
from scipy import stats


Vin = open('exp 2 10k resistor/Vin.txt', 'r').read().split()
I10K = open('exp 2 10k resistor/I.txt', 'r').read().split()

linear_i = []
linear_v = []


i = 0
for x in Vin:
    val = float(x)
    Vin[i]= val
    i = i+1

i = 0
found = False
for x in I10K:
    val = float(x)
    I10K[i]= val
    if val > .000005 and not found:
        print(Vin[i])
        von10k = Vin[i]
        found = True
    if Vin[i] > von10k:
        linear_i.append(val)
        linear_v.append(Vin[i])
    i = i+1


title = "Plot of Voltage Vs Current"
xLabel = "Voltage In (V)"
yLabel = "Current Out (A)"
linear_v = np.array(linear_v)
linear_i = np.array(linear_i)
intercept = von10k
slope = 1.0/10000.0


Data = plt.plot(Vin, I10K, 'bo', markersize=3, label="10K Ohm Resistor")
Data = plt.plot(linear_v, slope*(linear_v-von10k), 'r', label="fitted line")


plt.legend()
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.grid(True)
plt.show()
