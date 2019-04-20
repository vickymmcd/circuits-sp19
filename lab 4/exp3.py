import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

Ix = open('exp3/294k-sink/Ix.txt', 'r').read().split()
Iz1 = open('exp3/2.94k-sink/Iz.txt', 'r').read().split()
Iz2 = open('exp3/28k-sink/Iz.txt', 'r').read().split()
Iz3 = open('exp3/294k-sink/Iz.txt', 'r').read().split()

iy1 = .23/(2940)
iy2 = .23/(28000)
iy3 = .23/(294000)

iz_theo1 = []
iz_theo2 = []
iz_theo3 = []

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
    iz_theo1.append(Ix[i]**2/iy1)
    iz_theo2.append(Ix[i]**2/iy2)
    iz_theo3.append(Ix[i]**2/iy3)

    i = i+1


#slope, intercept, r_value, p_value, std_err = stats.linregress(linear_v, linear_i)
#linear_v = np.array(linear_v)



if __name__ == '__main__':
    title = "Log Log Plot of Output Current for Current Sink"
    xLabel = "Ix (A)"
    yLabel = "Iz (A)"

    Data = plt.loglog(Ix, Iz1, 'bo', markersize=3, label="Iy1= "+str(iy1) + " A")
    Data = plt.loglog(Ix, Iz2, 'ro', markersize=3, label="Iy2= "+str(iy2) + " A")
    Data = plt.loglog(Ix, Iz3, 'go', markersize=3, label="Iy3= "+str(iy3) + " A")

    Data = plt.loglog(Ix, iz_theo1, 'b-', markersize=3, label="Iy1 theoretical")
    Data = plt.loglog(Ix, iz_theo2, 'r-', markersize=3, label="Iy2 theoretical")
    Data = plt.loglog(Ix, iz_theo3, 'g-', markersize=3, label="Iy3 theoretical")



    plt.legend()
    plt.ylim(10e-8, 10e-2)
    plt.savefig('Exp3_Sink.png', format='png')
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.grid(True)
    plt.show()
