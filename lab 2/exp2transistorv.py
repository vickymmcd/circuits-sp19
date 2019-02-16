
# Simple I-V Graph


import numpy as np
import matplotlib.pyplot as plt


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

i = 0
for x in Vin:
    val = float(x)
    Vin[i]= val
    i = i+1

i = 0
for x in Vt10K:
    val = float(x)
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

print(len(Vt10K))
print(len(Vin))
i = 0
for val in Vin:
    frac = val / Vt10K[i]
    frac2 = val / Vt1K[i]
    frac3 = val / Vt100[i]
    ion10k.append((frac*I10K[i])/(1-frac))
    ion1k.append((frac2*I1K[i])/(1-frac2))
    ion100.append((frac3*I100[i])/(1-frac3))
    i = i+1

ion10k_val = np.mean(ion10k)
print(ion10k_val)
ion1k_val = np.mean(ion1k)
print(ion1k_val)


if __name__ == '__main__':
    title = "Plot of Voltage Across the Transistor"
    xLabel = "Voltage In (V)"
    yLabel = "Voltage Across Transistor (V)"


    Data = plt.plot(Vin, Vt10K, 'bo', markersize=3, label="10K Ohm Resistor")
    Data = plt.plot(Vin, Vt1K, 'ro', markersize=3, label="1100 Ohm Resistor")
    Data = plt.plot(Vin, Vt100, 'go', markersize=3, label="110 Ohm Resistor")

    plt.legend()
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.grid(True)
    plt.show()
