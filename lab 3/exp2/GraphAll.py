

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

# Exp 1 Data
Exp1_Ib = open('../exp1/Ib.txt', 'r').read().split()
Exp1_Ie = open('../exp1/Ie.txt', 'r').read().split()
Exp1_Vb = open('../exp1/Vb.txt', 'r').read().split()

I_c_100 = []
I_c_1K = []
I_c_10K = []

Exp1_Ic = []

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

i = 0
for x in I_b_1K:
    I_bval = float(x)
    I_eval = float(I_e_1K[i])
    I_b_1K[i] = I_bval
    I_e_1K[i] = I_eval
    V_b_1K[i] = float(V_b_1K[i])
    I_c_1K.append((-1*I_eval) - I_bval)
    i = i+1

i = 0
for x in I_b_10K:
    I_bval = float(x)
    I_eval = float(I_e_10K[i])
    I_b_10K[i] = I_bval
    I_e_10K[i] = I_eval
    V_b_10K[i] = float(V_b_10K[i])
    I_c_10K.append((-1*I_eval) - I_bval)
    i = i+1

i = 0
for x in Exp1_Ib:
    I_bval = float(x)
    I_eval = float(Exp1_Ie[i])
    Exp1_Ib[i] = I_bval
    Exp1_Ie[i] = I_eval
    Exp1_Vb[i] = float(Exp1_Vb[i])
    Exp1_Ic.append((-1*I_eval) - I_bval)
    i = i+1

# Setting up plot
title = "Collector Current Vs Base Voltage"
xLabel = "Vb (Volts)"
yLabel = "Ic (Amps)"

# Exp1 Theoretical

Exp1_Ic_Theo = []

slope, intercept, r_value, p_value, std_err = stats.linregress(Exp1_Vb,Exp1_Ic)
U_T = (1/slope)



for x in Exp1_Vb:
    Exp1_Ic_Theo.append(1e-12*math.exp(x/U_T*1000))


# Plotting Data

Data1 = plt.semilogy(V_b_100, I_c_100, 'ro', markersize=3, label="R = 100 Ohm")
Data2 = plt.semilogy(V_b_1K, I_c_1K, 'bo', markersize=3, label="R = 1K Ohm")
Data3 = plt.semilogy(V_b_10K, I_c_10K, 'go', markersize=3, label="R = 10K Ohm")
Data4 = plt.semilogy(Exp1_Vb, Exp1_Ic , 'k-', markersize=3, label="Collector Characteristic w/o Resistor")
Data5 = plt.semilogy(Exp1_Vb, Exp1_Ic_Theo , 'p-', markersize=3, label="Theoretical Collector Characteristic w/o Resistor")

# More plot settings
plt.legend()
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
#plt.xticks([0,1,3])
#plt.xlim(V_b_100[0], V_b_100[49])
#plt.axis([min(I_b_100) ,max(I_b_100) , min(I_c_100) , max(I_c_100)])
plt.show()

#Finding the unit differnce for pretty graphing
# maxX = max(VC_VoltageVal)
# minX = min(VC_VoltageVal)
# maxY = max(VC_CurrentVal)
# minY = min(VC_CurrentVal)
# stdUnitX = VC_VoltageVal[10]-VC_VoltageVal[8]
# stdUnitY = -2 #VC_CurrentVal[10]-VC_CurrentVal[8]




# slope, intercept, r_value, p_value, std_err = stats.linregress(VC_VoltageVal,VC_CurrentVal)
# U_T = (1/slope)
# I_s = math.exp(intercept)
#
# # xx = np.linspace(minX, maxX)
# # yy = exponenial_func(xx, *popt)
# #Best_fit = plt.plot( xx, yy, 'k--', label="Best Fit Fit ")
# v = np.polyfit(np.log(xx), yy, 1)
# slope, intercept, r_value, p_value, std_err = stats.linregress(xx, yy)
# # print(slope, intercept, "____")
#
# #Finding the theoretical curve
#
# #V/C Characteristic Thero
# xthero = VC_VoltageVal
# ythero = [ I_s* math.exp(xi/U_T) for xi in xthero]
# Theoretical_Curve = plt.semilogy(xthero, ythero, 'k--', markersize=3, label="Theoretical Fit ")
# #
# # #rD Thero
# # rD_X_thero = np.linspace(minX,maxX)
# # rD_y_ythero = [ math.log(-1*intercept) + math.log(xi/(1/slope)) for xi in xthero]
# # rD_Theoretical_Curve = plt.semilogx(xthero, ythero, 'ko', label="Theoretical Fit ")
#

#
# #Finding rd
# #rD = np.divide(np.diff(VC_VoltageVal), np.diff(VC_CurrentVal))
#
