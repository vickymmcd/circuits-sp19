
# Simple I-V Graph


import numpy as np
import matplotlib.pyplot as plt
from exp2graph10k import von10k
from exp2graph1k import von1k
from exp2graph100 import von100
from exp2graphall import ut, iss

xs = [110, 1100, 10000]
ys = [von100, von1k, von10k]
vons = []

for val in xs:
    ion = ut/val
    von = ut*np.log(ion/iss)
    vons.append(von)

if __name__ == '__main__':
    title = "Plot of Resistance Versus Von"
    xLabel = "Resistance (Ohms)"
    yLabel = "Von (Volts)"


    Data = plt.plot(xs, ys, 'bx', markersize=8, label="Experimental")
    Data = plt.plot(xs, vons, 'ro', markersize=5, label="Theoretical")

    plt.legend()
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.grid(True)
    plt.show()
