

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

G_m100 = []
G_m1K = []
G_m10K = []

Theo_Gm_100 = []
Theo_Gm_1K = []
Theo_Gm_10K = []

B = 998
U_t = 0.34
#Calc I_c
i = 0
for x in I_b_100:
    I_bval = float(x)
    I_eval = float(I_e_100[i])
    I_b_100[i] = I_bval
    I_e_100[i] = I_eval
    V_b_100[i] = float(V_b_100[i])
    I_c_100.append((-1*I_eval) - I_bval)
    R = 100
    gm = I_c_100[i]/U_t #Ic/Ut
    re = U_t/(-1*I_eval)#Ut/Ie
    Theo_Gm_100.append(gm/(1+(R/re)))

    if(i != 0):
        yc = float(I_c_100[i])-float(I_c_100[i-1])
        xc = float(V_b_100[i])-float(V_b_100[i-1])
        G_m100.append((yc)/(xc))
    else:
        G_m100.append(0)
    i = i+1

i = 0
for x in I_b_1K:
    I_bval = float(x)
    I_eval = float(I_e_1K[i])
    I_b_1K[i] = I_bval
    I_e_1K[i] = I_eval
    V_b_1K[i] = float(V_b_1K[i])
    I_c_1K.append((-1*I_eval) - I_bval)
    R = 1000
    gm = I_c_1K[i]/U_t #Ic/Ut
    re = U_t/(-1*I_eval)#Ut/Ie
    Theo_Gm_1K.append(gm/(1+(R/re)))

    if(i != 0):
        yc = float(I_c_1K[i])-float(I_c_1K[i-1])
        xc = float(V_b_1K[i])-float(V_b_1K[i-1])
        G_m1K.append((yc)/(xc))
    else:
        G_m1K.append(0)
    i = i+1

i = 0
for x in I_b_10K:
    I_bval = float(x)
    I_eval = float(I_e_10K[i])
    I_b_10K[i] = I_bval
    I_e_10K[i] = I_eval
    V_b_10K[i] = float(V_b_10K[i])
    I_c_10K.append((-1*I_eval) - I_bval)
    R = 10000
    gm = I_c_10K[i]/U_t #Ic/Ut
    re = U_t/(-1*I_eval)#Ut/Ie
    Theo_Gm_10K.append(gm/(1+(R/re)))

    if(i != 0):
        yc = float(I_c_10K[i])-float(I_c_10K[i-1])
        xc = float(V_b_10K[i])-float(V_b_10K[i-1])
        G_m10K.append((yc)/(xc))
    else:
        G_m10K.append(0)
    i = i+1

    

# Setting up plot
title = "Incremental Transconductance Gain vs Collector Current"
yLabel = "Gm: Change in Ic/Vb (Volts/Amps)"
xLabel = "Ic (Amps)"

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

Data1 = plt.loglog(I_c_100, G_m100, 'ro', markersize=3, label="R = 100 Ohm")
Data2 = plt.loglog(I_c_1K, G_m1K, 'bo', markersize=3, label="R = 1K Ohm")
Data3 = plt.loglog(I_c_10K, G_m10K, 'go', markersize=3, label="R = 10K Ohm")
Data4 = plt.loglog(I_c_100, Theo_Gm_100, 'c^', markersize=4, label="R = 100 Ohm Theoretical")
Data5 = plt.loglog(I_c_1K, Theo_Gm_1K, 'm^', markersize=4, label="R = 1K Ohm Theoretical")
Data6 = plt.loglog(I_c_10K, Theo_Gm_10K, 'k^', markersize=4, label="R = 10K Ohm Theoretical")

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
