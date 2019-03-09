import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

Ix = open('exp32/2.94k-sink/Ix.txt', 'r').read().split()
Iz1 = open('exp32/2.94k-sink/Iz.txt', 'r').read().split()
Iz2 = open('exp32/28k-sink/Iz.txt', 'r').read().split()
Iz3 = open('exp32/294k-sink/Iz.txt', 'r').read().split()


i = 0
for x in Ix:
    val = float(x)
    Ix[i]= val
    i = i+1

i = 0
for x in Iz1:
    val = -1*float(x)
    Iz1[i]= val
    i = i+1

i = 0
for x in Iz2:
    val = -1*float(x)
    Iz2[i]= val
    i = i+1

i = 0
for x in Iz3:
    val = -1*float(x)
    Iz3[i]= val
    i = i+1


#slope, intercept, r_value, p_value, std_err = stats.linregress(linear_v, linear_i)
#linear_v = np.array(linear_v)



if __name__ == '__main__':
    title = "Plot of current versus current fix me"
    xLabel = "Ix (A)"
    yLabel = "Iz (A)"

    Data = plt.loglog(Ix, Iz1, 'bo', markersize=3, label="2.94K Ohms")
    Data = plt.loglog(Ix, Iz2, 'ro', markersize=3, label="28K Ohms")
    Data = plt.loglog(Ix, Iz3, 'go', markersize=3, label="294K Ohms")



    plt.legend()
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.grid(True)
    plt.show()
