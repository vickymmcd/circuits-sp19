
# Simple I-V Graph


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

Vb = open('exp4-200/Vb.txt', 'r').read().split()
Vout = open('exp4-200/Vout.txt', 'r').read().split()
Vout2 = open('exp4-300/Vout.txt', 'r').read().split()
Vout3 = open('exp4-400/Vout.txt', 'r').read().split()


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

i = 0
for x in Vout2:
    val = float(x)
    Vout2[i]= val
    i = i+1

i = 0
for x in Vout3:
    val = float(x)
    Vout3[i]= val
    i = i+1



if __name__ == '__main__':
    title = "Plot of Voltage Transfer Characteristic"
    xLabel = "Voltage In (V)"
    yLabel = "Voltage Out (V)"

    Data = plt.plot(Vb, Vout, 'bo', markersize=3, label="200 Ohm Resistor")
    Data = plt.plot(Vb, Vout2, 'ro', markersize=3, label="300 Ohm Resistor")
    Data = plt.plot(Vb, Vout3, 'go', markersize=3, label="400 Ohm Resistor")


    plt.legend()
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.grid(True)
    plt.show()
