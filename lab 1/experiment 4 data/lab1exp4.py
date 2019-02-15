

# Simple I-V Graph


import numpy as np
import matplotlib.pyplot as plt


def best_fit(X, Y):

    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X) # or len(Y)

    numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in X]) - n * xbar**2

    b = numer / denum
    a = ybar - b * xbar
    print(a)
    print(b)
    # print('best fit line:\ny = {:.2f} + {:.2f}x'.format(a, b))

    return a, b

def get_theoretical_I(position, V):
    return ((1.0/(2.0**(position+1))*(V/10000)))*1000

I1bVals = open('1b measurements/I1b.txt', 'r').read().split()
I2bVals = open('2b measurements/I2b.txt', 'r').read().split()
I3bVals = open('3b measurements/I3b.txt', 'r').read().split()
I4bVals = open('4b measurements/I4b.txt', 'r').read().split()

VinVals = open('1b measurements/Vin.txt', 'r').read().split()
position = [1,2,3,4]

i = 0
for x in I1bVals:
    val = float(x) * -1000
    I1bVals[i]= val
    i = i+1

i = 0
for x in I2bVals:
    val = float(x) * -1000
    I2bVals[i]= val
    i = i+1

i = 0
for x in I3bVals:
    val = float(x) * -1000
    I3bVals[i]= val
    i = i+1

i = 0
for x in I4bVals:
    val = float(x) * -1000
    I4bVals[i]= val
    i = i+1

i = 0
for x in VinVals:
    val = float(x)
    VinVals[i]= val
    i = i+1

print(len(I1bVals))
print(len(I1bVals)/2)
yvals = [I1bVals[len(I1bVals)/2], I2bVals[len(I2bVals)/2], I3bVals[len(I3bVals)/2], I4bVals[len(I4bVals)/2]]
yvals2 = [I1bVals[len(I1bVals)-1], I2bVals[len(I2bVals)-1], I3bVals[len(I3bVals)-1], I4bVals[len(I4bVals)-1]]
print("voltage value ", VinVals[len(VinVals)/2])

"""
maxX = max(I1bVals)
minX = min(I1bVals)
maxY = max(VinVals)
minY = min(VinVals)


a, b = best_fit(I1bVals, VinVals)
xthero = np.linspace(0,5)
ythero = [0.5 * xi for xi in xthero]
# Line = plt.plot(XVals, yfit, 'r', label="Line of Best Fit")
#plt.plot(np.unique(XVals), np.poly1d(np.polyfit(XVals, YVals, 1))(np.unique(XVals)),'r', label="Line of Best Fit")
Line = plt.plot(xthero, ythero, 'r', label="Theoretical Fit ")
"""

title = "Semilog Plot of Position Vs Current"
xLabel = "Position (Unit Ladders)"
yLabel = "Current Out (mA)"

yvals3 = [get_theoretical_I(1, VinVals[len(VinVals)/2]), get_theoretical_I(2, VinVals[len(VinVals)/2]), get_theoretical_I(3, VinVals[len(VinVals)/2]), get_theoretical_I(4, VinVals[len(VinVals)/2])]
yvals4 = [get_theoretical_I(1, VinVals[len(VinVals)-1]), get_theoretical_I(2, VinVals[len(VinVals)-1]), get_theoretical_I(3, VinVals[len(VinVals)-1]), get_theoretical_I(4, VinVals[len(VinVals)-1])]

Data = plt.semilogy(position, yvals, 'bo', markersize=3, label="Vin Experimental: " + str(VinVals[len(VinVals)/2]) + " V")
Data = plt.semilogy(position, yvals3, 'bx', markersize=6, label="Vin Theoretical: " + str(VinVals[len(VinVals)/2]) + " V")

Data = plt.semilogy(position, yvals2, 'ro', markersize=3, label="Vin Experimental: " + str(VinVals[len(VinVals)-1]) + " V")
Data = plt.semilogy(position, yvals4, 'rx', markersize=6, label="Vin Theoretical: " + str(VinVals[len(VinVals)-1]) + " V")
print(yvals3)

plt.legend()
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.grid(True)
plt.show()
