
import numpy as np
import math
import matplotlib.pyplot as plt
from numpy import *

# Importing Data
V1 = open('v2=2v/V1.txt', 'r').read().split()

Vout1 = open('v2=2v/Vout.txt', 'r').read().split()

Vout2 = open('v2=3v/Vout.txt', 'r').read().split()

Vout3 = open('v2=4v/Vout.txt', 'r').read().split()

i = 0
for x in V1:
    V1[i] = float(V1[i])
    Vout1[i] = float(Vout1[i])
    Vout2[i] = float(Vout2[i])
    Vout3[i] = float(Vout3[i])

    i+=1



if __name__ == "__main__":
    # Setting up plot
    title = "Voltage Transfer Characteristics"
    yLabel = "Vout (V)"
    xLabel = "V1 (V)"

    Data1 = plt.plot(V1, Vout1, 'ro', markersize=5, label="V2 = 2V")
    Data2 = plt.plot(V1, Vout2, 'go', markersize=4, label="V2 = 3V")
    Data3 = plt.plot(V1, Vout3, 'bo', markersize=3, label="V2 = 4V")

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.savefig('VTCs.png', format='png')
    plt.show()
