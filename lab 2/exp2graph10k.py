
# Simple I-V Graph


import numpy as np
import matplotlib.pyplot as plt
from exp2graphall import von10k
from scipy import stats


Vin = open('exp 2 10k resistor/Vin.txt', 'r').read().split()
I10K = open('exp 2 10k resistor/I.txt', 'r').read().split()

theoretical10K = []
linear_i = []
linear_v = []


i = 0
for x in Vin:
    val = float(x)
    Vin[i]= val
    theoretical10K.append(val/10000)
    i = i+1

i = 0
for x in I10K:
    val = float(x)
    I10K[i]= val
    if Vin[i] > von10k:
        linear_i.append(val)
        linear_v.append(Vin[i])
    i = i+1

slope, intercept, r_value, p_value, std_err = stats.linregress(linear_v, linear_i)
print("slope is ", slope)
print("intercept is ", intercept)


title = "Plot of Voltage Vs Current"
xLabel = "Voltage In (V)"
yLabel = "Current Out (A)"


Data = plt.plot(Vin, I10K, 'bo', markersize=3, label="10K Ohm Resistor")
#Data = plt.plot(Vin, theoretical10K, 'bx', markersize=3, label="10K Ohm Resistor")
Data = plt.plot(linear_v, intercept+slope*linear_v, 'r', label="fitted line")


plt.legend()
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.grid(True)
plt.show()
