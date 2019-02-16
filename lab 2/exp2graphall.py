
# Simple I-V Graph


import numpy as np
import matplotlib.pyplot as plt
from exp2graph10k import von10k
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
linear_v_10k = []
linear_i_10k = []

i = 0
for x in Vin:
    val = float(x)
    Vin[i]= val
    if val < von10k:
        if float(I10K[i]) > 0:
            linear_v_10k.append(val)
            linear_i_10k.append(np.log(float(I10K[i])))
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

slope, intercept, r_value, p_value, std_err = stats.linregress(linear_v_10k[5:], linear_i_10k[5:])
iss = np.exp(intercept)
ut = 1/slope
print("Is ", iss)
print("Ut ", ut)
linear_v_10k = np.array(linear_v_10k)

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
    Data = plt.semilogy(linear_v_10k, np.exp(slope*(linear_v_10k)+intercept), 'r', label="fitted line: y=e^("+str(round(slope, 5))+"x + " +str(round(intercept, 5)) + ")")
    #Data = plt.plot(linear_v[5:], linear_i[5:], 'r', label="fitted line")
    #Data = plt.semilogy(Vin, theoretical1K, 'rx', markersize=3, label="1100 Ohm Resistor")
    #Data = plt.semilogy(Vin, theoretical100, 'gx', markersize=3, label="110 Ohm Resistor")

    plt.legend()
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.grid(True)
    plt.show()
