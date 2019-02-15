
# Simple I-V Graph


import numpy as np
import matplotlib.pyplot as plt


Vin = open('exp 2 10k resistor/Vin.txt', 'r').read().split()
I10K = open('exp 2 10k resistor/I.txt', 'r').read().split()

theoretical10K = []


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
    i = i+1


title = "Plot of Voltage Vs Current"
xLabel = "Voltage In (V)"
yLabel = "Current Out (A)"


Data = plt.plot(Vin, I10K, 'bo', markersize=3, label="10K Ohm Resistor")
Data = plt.plot(Vin, theoretical10K, 'bx', markersize=3, label="10K Ohm Resistor")


plt.legend()
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.grid(True)
plt.show()
