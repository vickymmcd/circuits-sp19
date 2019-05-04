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

for i, v in enumerate(vgs):
    if i%6==0:
        vgs2.append(v)
        i12.append(i1[i])
        i22.append(i2[i])
        i32.append(i3[i])
        i42.append(i4[i])
        i52.append(i5[i])

for i, val in enumerate(i52):
    print(val/i1[1])
    i1_theo.append(16*val)
    i2_theo.append(8*val)
    i3_theo.append(4*val)
    i4_theo.append(2*val)

#print(i1_theo)

if __name__ == '__main__':
    title = "Plot of Current Vs Gate Voltage in Ladder Network"
    xLabel = "Vg (V)"
    yLabel = "I (A)"

    Data = plt.plot(vgs2, i12, 'bo', markersize=3, label="I1")
    # Data = plt.plot(vgs2, i22, 'ro', markersize=3, label="I2")
    # Data = plt.plot(vgs2, i32, 'go', markersize=3, label="I3")
    # Data = plt.plot(vgs2, i42, 'ko', markersize=3, label="I4")
    # Data = plt.plot(vgs2, i52, 'co', markersize=3, label="I5")

    Data = plt.plot(vgs2, i1_theo, 'r*', markersize=3, label="I1 theoretical")
    # Data = plt.plot(vgs2, i2_theo, 'g*', markersize=3, label="I2 theoretical")
    # Data = plt.plot(vgs2, i3_theo, 'k*', markersize=3, label="I3 theoretical")
    # Data = plt.plot(vgs2, i4_theo, 'c*', markersize=3, label="I4 theoretical")


    plt.legend()
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.grid(True)
    plt.savefig('currents.png', format='png')
    plt.show()
