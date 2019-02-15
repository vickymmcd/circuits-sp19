
# Simple I-V Graph


import numpy as np
import matplotlib.pyplot as plt
from exp2transistorv import ion10k_val

iss = (1*10**-15)
ut = .025
Vin = open('exp 2 10k resistor/Vin.txt', 'r').read().split()
I10K = open('exp 2 10k resistor/I.txt', 'r').read().split()
I1K = open('exp 2 1100 resistor/I.txt', 'r').read().split()
I100 = open('exp 2 110 resistor/I.txt', 'r').read().split()
theoretical10K = []
theoretical1K = []
theoretical100 = []

von10k = ut*np.log(ion10k_val/iss)
print(von10k)

i = 0
for x in Vin:
    val = float(x)
    Vin[i]= val
    #theoretical10K.append(val/10000)
    if val < von10k:
        theoretical10K.append((iss*(np.exp(val/ut))))
    else:
        theoretical10K.append(val/10000)
    theoretical1K.append(val/1100)
    theoretical100.append(val/110)
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


title = "Semilog Plot of Voltage Vs Current"
xLabel = "Voltage In (V)"
yLabel = "Current Out (A)"


Data = plt.semilogy(Vin, I10K, 'bo', markersize=3, label="10K Ohm Resistor")
Data = plt.semilogy(Vin, I1K, 'ro', markersize=3, label="1100 Ohm Resistor")
Data = plt.semilogy(Vin, I100, 'go', markersize=3, label="110 Ohm Resistor")
Data = plt.semilogy(Vin, theoretical10K, 'bx', markersize=3, label="10K Ohm Resistor")
#Data = plt.semilogy(Vin, theoretical1K, 'rx', markersize=3, label="1100 Ohm Resistor")
#Data = plt.semilogy(Vin, theoretical100, 'gx', markersize=3, label="110 Ohm Resistor")


plt.legend()
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.grid(True)
plt.show()
