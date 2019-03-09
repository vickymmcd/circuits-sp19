
# Simple I-V Graph


import numpy as np
import matplotlib.pyplot as plt
from exp2graph10k import von10k
from exp2graph1k import von1k
from exp2graph100 import von100
from exp2graphall import ut, iss

xs = [110, 1100, 10000]
ys = [von100, von1k, von10k]
ions = []

for val in xs:
    ion = ut/val
    ions.append(ion)

i = 0
for val in ys:
    ion = iss*np.exp(val/ut)
    ys[i] = ion

if __name__ == '__main__':
    title = "Plot of Resistance Versus Ion"
    xLabel = "Resistance (Ohms)"
    yLabel = "Ion (Amps)"


    Data = plt.loglog(xs, ys, 'bx', markersize=8, label="Experimental")
    Data = plt.loglog(xs, ions, 'ro', markersize=5, label="Theoretical")

    plt.legend()
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.grid(True)
    plt.show()
