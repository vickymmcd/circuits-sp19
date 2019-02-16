
# Simple I-V Graph


import numpy as np
import matplotlib.pyplot as plt
from exp2transistorv import ion10k_val, ion1k_val
from scipy import stats

iss = (1.0*10**-15)
ut = .025
Vin = open('exp 2 10k resistor/Vin.txt', 'r').read().split()
I10K = open('exp 2 10k resistor/I.txt', 'r').read().split()
I1K = open('exp 2 1100 resistor/I.txt', 'r').read().split()
I100 = open('exp 2 110 resistor/I.txt', 'r').read().split()
theoretical10K = []
theoretical1K = []
theoretical100 = []
linear_v = []
linear_i = []

von10k = ut*np.log(ion10k_val/iss)
von1k = ut*np.log(ion1k_val/iss)
print(von1k)

i = 0
for x in Vin:
    val = float(x)
    Vin[i]= val
    if val < .6:
        if float(I10K[i]) > 0:
            linear_v.append(val)
            linear_i.append(np.log(float(I10K[i])))
    theoretical1K.append(val/1100)
    theoretical100.append(val/110)
    i = i+1

i = 0
for x in I10K:
    val = float(x)
    I10K[i]= val
    i = i+1

i = 0
for x in I1K:
    val = float(x)
    I1K[i]= val
    i = i+1

i = 0
for x in I100:
    val = float(x)
    I100[i]= val
    i = i+1

slope, intercept, r_value, p_value, std_err = stats.linregress(linear_v[5:], linear_i[5:])
iss = np.exp(intercept)
ut = 1/slope
print("Is ", iss)
print("Ut ", ut)
linear_v = np.array(linear_v)

i = 0
for val in Vin:
    if val < .6:
        theoretical10K.append((iss*(np.exp(val/ut))))
    else:
        theoretical10K.append((val-.6)/10000)

if __name__ == '__main__':
    title = "Semilog Plot of Voltage Vs Current"
    xLabel = "Voltage In (V)"
    yLabel = "Current Out (A)"


    Data = plt.semilogy(Vin, I10K, 'bo', markersize=3, label="10K Ohm Resistor")
    Data = plt.semilogy(Vin, I1K, 'ro', markersize=3, label="1100 Ohm Resistor")
    Data = plt.semilogy(Vin, I100, 'go', markersize=3, label="110 Ohm Resistor")
    Data = plt.semilogy(Vin[2:], theoretical10K[2:], 'bx', markersize=5, label="10K Ohm Resistor")
    Data = plt.semilogy(linear_v, np.exp(slope*(linear_v)+intercept), 'r', label="fitted line")
    #Data = plt.plot(linear_v[5:], linear_i[5:], 'r', label="fitted line")
    #Data = plt.semilogy(Vin, theoretical1K, 'rx', markersize=3, label="1100 Ohm Resistor")
    #Data = plt.semilogy(Vin, theoretical100, 'gx', markersize=3, label="110 Ohm Resistor")


    plt.legend()
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.grid(True)
    plt.show()
