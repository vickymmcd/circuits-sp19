import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import stats
import matplotlib.ticker as plticker
from consts import U_t
from consts import I_s
Exp1_Ib = open('../exp1/Ib.txt', 'r').read().split()
Exp1_Ie = open('../exp1/Ie.txt', 'r').read().split()
Exp1_Vb = open('../exp1/Vb.txt', 'r').read().split()
i = 0
Exp1_Ic_Theo = []
Exp1_Ic = []
Exp1_Ib_Theo = []

for x in Exp1_Ib:
    I_bval = float(x)
    I_eval = float(Exp1_Ie[i])
    Exp1_Ib[i] = I_bval
    Exp1_Ie[i] = I_eval
    Exp1_Vb[i] = float(Exp1_Vb[i])
    Exp1_Ic.append((-1*I_eval) - I_bval)
    print("appending")
    i = i+1
linear_v = []
linear_i = []
beta_vals = []

V_bVals = []
I_cVals = []

# plt.figure(0)
# title = "Current Gain"
# xLabel = "Collector Current (A)"
# yLabel = "Base Current (A)"
# Data = plt.semilogy(Exp1_Ic, Exp1_Ib , 'k-', markersize=3, label="none")
# plt.legend()
# plt.xlabel(xLabel)
# plt.ylabel(yLabel)
# plt.title(title)
# loc = plticker.MultipleLocator(base=100) # this locator puts ticks at regular intervals
# plt.grid(True)
# plt.show()
slope, intercept, r_value, p_value, std_err = stats.linregress(Exp1_Vb,Exp1_Ic)
#U_t = (1/slope)
for x in Exp1_Vb:
     Exp1_Ib_Theo.append(I_s*math.exp(x/U_t)/100)

for x in Exp1_Vb:
     Exp1_Ic_Theo.append(I_s*math.exp(x/U_t))
print (Exp1_Ic_Theo)
if __name__ == '__main__':
 plt.figure(0)
 title = "Collector Current and Base Current vs Base Voltage"
 xLabel = "Voltage In (V)"
 yLabel = "Current(A)"
 Data = plt.semilogy(Exp1_Vb, Exp1_Ic , 'ko', markersize=3, label="Collector Characteristic w/o Resistor")
 Data1 = plt.semilogy(Exp1_Vb, Exp1_Ic_Theo , 'r-', markersize=3, label="Theoretical Collector Characteristic w/o Resistor")
 Data = plt.semilogy(Exp1_Vb, Exp1_Ib , 'bo', markersize=3, label="Base Characteristic w/o Resistor")
 Data1 = plt.semilogy(Exp1_Vb, Exp1_Ib_Theo , 'm-', markersize=3, label="Theoretical Base Characteristic w/o Resistor")
 plt.legend()
 plt.xlabel(xLabel)
 plt.ylabel(yLabel)
 plt.title(title)
 loc = plticker.MultipleLocator(base=100) # this locator puts ticks at regular intervals
 plt.grid(True)
 plt.show()
