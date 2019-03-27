import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import stats
import matplotlib.ticker as plticker
# from consts import U_t
# from consts import I_s
Exp1_Ib = open('one/Ib.txt', 'r').read().split()
Exp1_Ie = open('one/Ie.txt', 'r').read().split()
Exp1_Vb = open('one/Vb.txt', 'r').read().split()

Exp2_Ib = open('two/Ib.txt', 'r').read().split()
Exp2_Ie = open('two/Ie.txt', 'r').read().split()
Exp2_Vb = open('two/Vb.txt', 'r').read().split()

Exp3_Ib = open('three/Ib.txt', 'r').read().split()
Exp3_Ie = open('three/Ie.txt', 'r').read().split()
Exp3_Vb = open('three/Vb.txt', 'r').read().split()

Exp4_Ib = open('four/Ib.txt', 'r').read().split()
Exp4_Ie = open('four/Ie.txt', 'r').read().split()
Exp4_Vb = open('four/Vb.txt', 'r').read().split()
i = 0
f=0
j=0
k=0

Exp1_Ic = []
Exp2_Ic = []
Exp3_Ic = []
Exp4_Ic = []

for x in Exp1_Ib:
    I_bval = float(x)
    I_eval = float(Exp1_Ie[i])
    Exp1_Ib[i] = I_bval
    Exp1_Ie[i] = I_eval
    Exp1_Vb[i] = float(Exp1_Vb[i])
    Exp1_Ic.append((-1*I_eval) - I_bval)
    print("appending")
    i = i+1

for x in Exp2_Ib:
    I_bval = float(x)
    I_eval = float(Exp2_Ie[f])
    Exp2_Ib[f] = I_bval
    Exp2_Ie[f] = I_eval
    Exp2_Vb[f] = float(Exp2_Vb[f])
    Exp2_Ic.append((-1*I_eval) - I_bval)
    print("appending")
    f = f+1

for x in Exp3_Ib:
    I_bval = float(x)
    I_eval = float(Exp3_Ie[j])
    Exp3_Ib[j] = I_bval
    Exp3_Ie[j] = I_eval
    Exp3_Vb[j] = float(Exp3_Vb[j])
    Exp3_Ic.append((-1*I_eval) - I_bval)
    print("appending")
    j = j+1

for x in Exp4_Ib:
    I_bval = float(x)
    I_eval = float(Exp4_Ie[k])
    Exp4_Ib[k] = I_bval
    Exp4_Ie[k] = I_eval
    Exp4_Vb[k] = float(Exp4_Vb[k])
    Exp4_Ic.append((-1*I_eval) - I_bval)
    print("appending")
    k = k+1
# linear_v = []
# linear_i = []
# beta_vals = []
# V_bVals = []
# I_cVals = []
# slope, intercept, r_value, p_value, std_err = stats.linregress(Exp1_Vb,Exp1_Ic)
# print (Exp1_Ic_Theo)
if __name__ == '__main__':
 plt.figure(0)
 title = "Collector Current and Base Current vs Base Voltage"
 xLabel = "Voltage In (V)"
 yLabel = "Current(A)"
 Data = plt.semilogy(Exp1_Vb, Exp1_Ic , 'bo', markersize=3, label="Q1 Collector Characteristic")
 Data = plt.semilogy(Exp1_Vb, Exp1_Ib , 'b*', markersize=3, label="Q1 Base Characteristic")

 Data = plt.semilogy(Exp2_Vb, Exp2_Ic , 'ro', markersize=3, label="Q2 Collector Characteristic")
 Data = plt.semilogy(Exp2_Vb, Exp2_Ib , 'r*', markersize=3, label="Q2 Base Characteristic")

 Data = plt.semilogy(Exp3_Vb, Exp3_Ic , 'ko', markersize=3, label="Q3 Collector Characteristic")
 Data = plt.semilogy(Exp3_Vb, Exp3_Ib , 'k*', markersize=3, label="Q3 Base Characteristic")

Data = plt.semilogy(Exp4_Vb, Exp4_Ic , 'bo', markersize=3, label="Q4 Collector Characteristic")
Data = plt.semilogy(Exp4_Vb, Exp4_Ib , 'b*', markersize=3, label="Q4 Base Characteristic")

plt.legend()
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
loc = plticker.MultipleLocator(base=100) # this locator puts ticks at regular intervals
plt.grid(True)
plt.show()
