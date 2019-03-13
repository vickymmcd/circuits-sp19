

# Simple I-V Graph
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats
from Calcs import U_t, I_s, alpha

# Importing Data

I_b_100 = open('exp2-100/Ib.txt', 'r').read().split()
I_e_100 = open('exp2-100/Ie.txt', 'r').read().split()
V_b_100 = open('exp2-100/Vb.txt', 'r').read().split()

I_c_100 = []
Theo_100 = []

#Calc I_c
i = 0
for x in I_b_100:
    I_bval = float(x)
    I_eval = float(I_e_100[i])
    I_b_100[i] = I_bval
    I_e_100[i] = I_eval
    V_b_100[i] = float(V_b_100[i])
    I_c_100.append((-1*I_eval) - I_bval)
    i = i+1

print(U_t)
R = 100
i = 0
for x in I_c_100:
    I_eval = -1*float(I_e_100[i])
    Theo_100.append(I_eval* alpha)
    i = i+1

# Ut = []
# i = 0
#
# slope, intercept, r_value, p_value, std_err = stats.linregress(I_b_100,V_b_100)
#
# for x in V_b_100:
#     I_bval = float(I_b_100[i])
#     Ut.append(slope*I_bval)
#     i = i+1
#
# Data1 = plt.plot(I_b_100, Ut, 'ro', markersize=3, label="R = 100 Ohm")
# Setting up plot
title = "Collector Current Vs Base Voltage"
xLabel = "Vb (Volts)"
yLabel = "Ic (Amps)"

# Exp1 Theoretical

# Exp1_Ic_Theo = []
#
# slope, intercept, r_value, p_value, std_err = stats.linregress(Exp1_Vb,Exp1_Ic)
# U_T = (1/slope)
#
# for x in Exp1_Vb:
#     Exp1_Ic_Theo.append(1e-12*math.exp(x/U_T*1000))


# Plotting Data

Data1 = plt.plot(V_b_100, I_c_100, 'bo', markersize=3, label="R = 100 Ohm")
Data2 = plt.plot(V_b_100, Theo_100, 'k--', markersize=3, label="Theoretical Fit")
# Data3 = plt.semilogy(V_b_100, I_c_100, 'go', markersize=3, label="R = 100 Ohm")
# Data4 = plt.semilogy(Exp1_Vb, Exp1_Ic , 'k-', markersize=3, label="Collector Characteristic w/o Resistor")
# Data5 = plt.semilogy(Exp1_Vb, Exp1_Ic_Theo , 'p-', markersize=3, label="Theoretical Collector Characteristic w/o Resistor")

# More plot settings
plt.legend()
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.show()
