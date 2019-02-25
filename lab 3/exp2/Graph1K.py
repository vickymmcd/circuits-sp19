

# Simple I-V Graph
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats

# Importing Data

I_b_1K = open('exp2-1K/Ib.txt', 'r').read().split()
I_e_1K = open('exp2-1K/Ie.txt', 'r').read().split()
V_b_1K = open('exp2-1K/Vb.txt', 'r').read().split()

I_c_1K = []
Theo_1K = []

#Calc I_c
i = 0
for x in I_b_1K:
    I_bval = float(x)
    I_eval = float(I_e_1K[i])
    I_b_1K[i] = I_bval
    I_e_1K[i] = I_eval
    V_b_1K[i] = float(V_b_1K[i])
    I_c_1K.append((-1*I_eval) - I_bval)
    i = i+1

R = 1000
i = 0
for x in I_c_1K:
    U_t = 0.34;
    I_eval = -1*float(I_e_1K[i])
    V_bval = float(V_b_1K[i])
    gm = x/U_t
    re = U_t/I_eval
    slope = gm/(1+(R/re))
    Theo_1K.append(slope* V_bval)
    i = i+1

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

Data1 = plt.plot(V_b_1K, I_c_1K, 'ro', markersize=3, label="R = 1K Ohm")
Data2 = plt.plot(V_b_1K, Theo_1K, 'bo', markersize=3, label="Theoretical Fit")
# Data3 = plt.semilogy(V_b_10K, I_c_10K, 'go', markersize=3, label="R = 10K Ohm")
# Data4 = plt.semilogy(Exp1_Vb, Exp1_Ic , 'k-', markersize=3, label="Collector Characteristic w/o Resistor")
# Data5 = plt.semilogy(Exp1_Vb, Exp1_Ic_Theo , 'p-', markersize=3, label="Theoretical Collector Characteristic w/o Resistor")

# More plot settings
plt.legend()
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.show()
