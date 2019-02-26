

# Simple I-V Graph
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats

# Importing Data
#100 Ohm
I_b_100 = open('exp2-100/Ib.txt', 'r').read().split()
I_e_100 = open('exp2-100/Ie.txt', 'r').read().split()
V_b_100 = open('exp2-100/Vb.txt', 'r').read().split()
#1K Ohm
I_b_1K = open('exp2-1k/Ib.txt', 'r').read().split()
I_e_1K = open('exp2-1k/Ie.txt', 'r').read().split()
V_b_1K = open('exp2-1k/Vb.txt', 'r').read().split()
#10K Ohm
I_b_10K = open('exp2-10k/Ib.txt', 'r').read().split()
I_e_10K = open('exp2-10k/Ie.txt', 'r').read().split()
V_b_10K = open('exp2-10k/Vb.txt', 'r').read().split()


I_c_100 = []
I_c_1K = []
I_c_10K = []

R_b100 = []
R_b1K = []
R_b10K = []

Theo_Rb_100 = []
Theo_Rb_1K = []
Theo_Rb_10K = []

B = 100
#Calc I_c
i = 0
for x in I_b_100:
    I_bval = float(x)
    I_eval = float(I_e_100[i])
    I_b_100[i] = I_bval
    I_e_100[i] = I_eval
    V_b_100[i] = float(V_b_100[i])
    I_c_100.append((-1*I_eval) - I_bval)
    Theo_Rb_100.append((B+1)*100 + (0.34/I_bval))

    if(i != 0):
        yc = float(V_b_100[i])-float(V_b_100[i-1])
        xc = float(I_b_100[i])-float(I_b_100[i-1])
        R_b100.append((yc)/(xc))
    else:
        R_b100.append(0)
    i = i+1

i = 0
for x in I_b_1K:
    I_bval = float(x)
    I_eval = float(I_e_1K[i])
    I_b_1K[i] = I_bval
    I_e_1K[i] = I_eval
    V_b_1K[i] = float(V_b_1K[i])
    I_c_1K.append((-1*I_eval) - I_bval)
    Theo_Rb_1K.append((B+1)*1000 + (0.34/I_bval))

    if(i != 0):
        yc = float(V_b_1K[i])-float(V_b_1K[i-1])
        xc = float(I_b_1K[i])-float(I_b_1K[i-1])
        R_b1K.append((yc)/(xc))
    else:
        R_b1K.append(0)
    i = i+1

i = 0
for x in I_b_10K:
    I_bval = float(x)
    I_eval = float(I_e_10K[i])
    I_b_10K[i] = I_bval
    I_e_10K[i] = I_eval
    V_b_10K[i] = float(V_b_10K[i])
    I_c_10K.append((-1*I_eval) - I_bval)
    Theo_Rb_10K.append((B+1)*10000 + (0.34/I_bval))

    if(i != 0):
        yc = float(V_b_10K[i])-float(V_b_10K[i-1])
        xc = float(I_b_10K[i])-float(I_b_10K[i-1])
        R_b10K.append((yc)/(xc))
    else:
        R_b10K.append(0)
    i = i+1



# Setting up plot
title = "Incremental Base Resistance vs Base Current"
yLabel = "Rb: Change in Vb/Ib (Volts/Amps)"
xLabel = "Ib (Amps)"

# Exp1 Theoretical

# Exp1_Ic_Theo = []
#
# slope, intercept, r_value, p_value, std_err = stats.linregress(Exp1_Vb,Exp1_Ic)
# U_T = (1/slope)
#
#
# for x in Exp1_Vb:
#     Exp1_Ic_Theo.append(1e-12*math.exp(x/U_T*1000))

# Plotting Data

Data1 = plt.loglog(I_b_100, R_b100, 'ro', markersize=3, label="R = 100 Ohm")
Data2 = plt.loglog(I_b_1K, R_b1K, 'bo', markersize=3, label="R = 1K Ohm")
Data3 = plt.loglog(I_b_10K, R_b10K, 'go', markersize=3, label="R = 10K Ohm")
Data4 = plt.loglog(I_b_100, Theo_Rb_100, 'c--', markersize=4, label="R = 100 Ohm Theoretical")
Data5 = plt.loglog(I_b_1K, Theo_Rb_1K, 'm--', markersize=4, label="R = 1K Ohm Theoretical")
Data6 = plt.loglog(I_b_10K, Theo_Rb_10K, 'k--', markersize=4, label="R = 10K Ohm Theoretical")

# More plot settings
plt.legend()
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
#plt.xticks([0,1,3])
#plt.xlim(V_b_100[0], V_b_100[49])
#plt.axis([min(I_b_100) ,max(I_b_100) , min(I_c_100) , max(I_c_100)])
plt.show()


#
