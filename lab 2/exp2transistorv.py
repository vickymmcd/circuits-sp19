
# Simple I-V Graph


import numpy as np
from exp2graph10k import von10k
import matplotlib.pyplot as plt
from scipy import stats


Vin = open('exp 2 10k resistor/Vin.txt', 'r').read().split()
Vt10K = open('exp 2 10k resistor/Vt.txt', 'r').read().split()
Vt1K = open('exp 2 1100 resistor/Vt.txt', 'r').read().split()
Vt100 = open('exp 2 110 resistor/Vt.txt', 'r').read().split()
I10K = open('exp 2 10k resistor/I.txt', 'r').read().split()
I1K = open('exp 2 1100 resistor/I.txt', 'r').read().split()
I100 = open('exp 2 110 resistor/I.txt', 'r').read().split()
ion10k = []
ion1k = []
ion100 = []
linear_vin = []
linear_vt = []

i = 0
for x in Vin:
    val = float(x)
    Vin[i]= val
    i = i+1

i = 0
for x in Vt10K:
    val = float(x)
    if Vin[i] < von10k:
        linear_vin.append(Vin[i])
        linear_vt.append(val)
    Vt10K[i]= val
    i = i+1

i = 0
for x in Vt1K:
    val = float(x)
    Vt1K[i]= val
    i = i+1

i = 0
for x in Vt100:
    val = float(x)
    Vt100[i]= val
    i = i+1

i = 0
for x in I10K:
    val = float(x)
    I10K[i]= val
    i = i+1

i = 0
for x in I1K:
    val = float(x)
    I1K[i]= val
    i = i+1

i = 0
for x in I100:
    val = float(x)
    I100[i]= val
    i = i+1

slope, intercept, r_value, p_value, std_err = stats.linregress(linear_vin, linear_vt)
linear_vin = np.array(linear_vin)


if __name__ == '__main__':
    title = "Plot of Voltage Across the Transistor"
    xLabel = "Voltage In (V)"
    yLabel = "Voltage Across Transistor (V)"


    Data = plt.plot(Vin, Vt10K, 'bo', markersize=3, label="10K Ohm Resistor")
    Data = plt.plot(Vin, Vt1K, 'ro', markersize=3, label="1100 Ohm Resistor")
    Data = plt.plot(Vin, Vt100, 'go', markersize=3, label="110 Ohm Resistor")
    Data = plt.plot(linear_vin, (slope*linear_vin)+intercept, 'r', label="fitted line: y="+str(round(slope, 5))+"x + " +str(round(intercept,5)))

    plt.legend()
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.grid(True)
    plt.show()
