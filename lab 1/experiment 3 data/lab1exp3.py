

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

XVals = open('Iin.txt', 'r').read().split()
YVals = open('Iout.txt', 'r').read().split()

i = 0
for x in YVals:
    val = float(x) * -1000
    print(val)
    YVals[i]= val
    i = i+1

i = 0
for x in XVals:
    val = float(x) * 1000
    XVals[i]= val
    i = i+1

maxX = max(XVals)
minX = min(XVals)
maxY = max(YVals)
minY = min(YVals)
stdUnitX = XVals[10]-XVals[8]
stdUnitY = YVals[10]-YVals[8]

a, b = best_fit(XVals, YVals)
xthero = np.linspace(0,5)
ythero = [0.5 * xi for xi in xthero]
# Line = plt.plot(XVals, yfit, 'r', label="Line of Best Fit")
#plt.plot(np.unique(XVals), np.poly1d(np.polyfit(XVals, YVals, 1))(np.unique(XVals)),'r', label="Line of Best Fit")
Line = plt.plot(xthero, ythero, 'r', label="Theoretical Fit ")


title = "Characteristic of Current Divider"
xLabel = "Current In (Amp)"
yLabel = "Current Out (Amp)"

Data = plt.plot(XVals, YVals, 'bo', markersize=3, label="Divider Ratio Value")

plt.legend()
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.axis([minX-stdUnitX , maxX+stdUnitX , minY - stdUnitY , maxY + stdUnitY])
plt.grid(True)
plt.show()
