import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

Ix = open('FinalProjectData.txt', 'r').read().split()
vgs =[]
i1 = []
i2 = []
i3 = []
i4 = []
i5 = []

vgs2 =[]
i12 = []
i22 = []
i32 = []
i42 = []
i52 = []

i1_theo = []
i2_theo = []
i3_theo = []
i4_theo = []
i5_theo = []

count = 0
for line in Ix:
    if "v2" in line:
        pass
    else:
        if count == 0:
            vgs.append(float(line))
        elif count == 2:
            i1.append(float(line))
        elif count == 3:
            i2.append(float(line))
        elif count == 4:
            i3.append(float(line))
        elif count == 5:
            i4.append(float(line))
        elif count == 6:
            i5.append(float(line))
            count = -1
        count += 1

ind = 0
for x in i1:
    i1_theo.append(x)
    i2_theo.append(2*x)
    i3_theo.append(4*x)
    i4_theo.append(8*x)
    i5_theo.append(16*x)
    ind+=1

x = 4

import numpy as np
vgs1 = np.asarray(vgs)
vgs = vgs1[::x] #Take every x element

i1 = np.asarray(i1)
i1 = i1[::x]

i1_theo1 = np.asarray(i1_theo)
i1_theo = i1_theo1[::x]

i2 = np.asarray(i2)
i2 = i2[::x]

i2_theo1 = np.asarray(i2_theo)
i2_theo = i2_theo1[::x]

i3 = np.asarray(i3)
i3 = i3[::x]

i3_theo1 = np.asarray(i3_theo)
i3_theo = i3_theo1[::x]

i4 = np.asarray(i4)
i4 = i4[::x]

i4_theo1 = np.asarray(i4_theo)
i4_theo = i4_theo1[::x]

i5 = np.asarray(i5)
i5 = i5[::x]

i5_theo1 = np.asarray(i5_theo)
i5_theo = i5_theo1[::x]



if __name__ == '__main__':
    title = "Plot of Current Vs Gate Voltage in Ladder Network"
    xLabel = "Vg (V)"
    yLabel = "I (A)"

    Data = plt.plot(vgs, i1, 'bo', markersize=3, label="I1")
    Data = plt.plot(vgs, i2, 'ro', markersize=3, label="I2")
    Data = plt.plot(vgs, i3, 'go', markersize=3, label="I3")
    Data = plt.plot(vgs, i4, 'ko', markersize=3, label="I4")
    Data = plt.plot(vgs, i5, 'co', markersize=3, label="I5")

    Data = plt.plot(vgs, i1_theo, 'b--', markersize=3, label="I1 theoretical")
    Data = plt.plot(vgs, i2_theo, 'r--', markersize=3, label="I2 theoretical")
    Data = plt.plot(vgs, i3_theo, 'g--', markersize=3, label="I3 theoretical")
    Data = plt.plot(vgs, i4_theo, 'k--', markersize=3, label="I4 theoretical")
    Data = plt.plot(vgs, i5_theo, 'c--', markersize=3, label="I5 theoretical")


    plt.legend()
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.grid(True)
    plt.savefig('currents.png', format='png')
    plt.show()
