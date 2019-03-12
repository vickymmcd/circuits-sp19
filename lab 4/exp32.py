import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

Iy = open('exp3/2500k-source/Iy.txt', 'r').read().split()
Iz1 = open('exp3/2500k-source/Iz.txt', 'r').read().split()
#Iz2 = open('exp32/ix2-source/negative/Iz.txt', 'r').read().split()
#Iz3 = open('exp32/ix3-source/negative/Iz.txt', 'r').read().split()

ix1 = 1.0*10**-6
ix2 = 1.0*10**-5
ix3 = 1.0*10**-4

iz_theo1 = []
iz_theo2 = []
iz_theo3 = []

i = 0
for x in Iy:
    val = -1*float(x)
    Iy[i]= val
    i = i+1

i = 0
for x in Iz1:
    val = -1*float(x)
    Iz1[i]= val
    iz_theo1.append(ix1**2/Iy[i])
    iz_theo2.append(ix2**2/Iy[i])
    iz_theo3.append(ix3**2/Iy[i])
    i = i+1

# i = 0
# for x in Iz2:
#     val = -1*float(x)
#     Iz2[i]= val
#     iz_theo2.append(ix2**2/Iy[i])
#     i = i+1
#
# i = 0
# for x in Iz3:
#     val = -1*float(x)
#     Iz3[i]= val
#     iz_theo3.append(ix3**2/Iy[i])
#     i = i+1




if __name__ == '__main__':
    title = "Plot of current versus current fix me"
    xLabel = "Iy (A)"
    yLabel = "Iz (A)"

    Data = plt.loglog(Iy, Iz1, 'bo', markersize=3, label="Ix1= "+str(ix1))
    #Data = plt.loglog(Iy, Iz2, 'ro', markersize=3, label="Ix2= "+str(ix2))
    #Data = plt.loglog(Iy, Iz3, 'go', markersize=3, label="Ix3= "+str(ix3))

    Data = plt.loglog(Iy, iz_theo1, 'b-', markersize=3, label="Ix1 theoretical")
    Data = plt.loglog(Iy, iz_theo2, 'r-', markersize=3, label="Ix2 theoretical")
    Data = plt.loglog(Iy, iz_theo3, 'g-', markersize=3, label="Ix3 theoretical")



    plt.legend()
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.grid(True)
    plt.show()
