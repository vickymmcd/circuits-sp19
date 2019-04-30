# -*- coding: utf-8 -*-

#Script to semilog-plot the channel current as a function of gate voltage of nMOS transistor
#Extracts Is, κ, and VT0
#Plots theoretical EKV model

import sys
sys.path.append('..')
from ekvfit import ekvfit

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats

# Importing Data
CcRaw = open('../pmos exp1-2/Id.txt', 'r').read().split() #Collector Current
VgRaw = open('../pmos exp1-2/Vg.txt', 'r').read().split() #Gate Voltage


Cc = []
Vg = []

TheoCC = []
Vd = 5
Ut = 0.025

#nMOS EKV current equation:
# I =Is log^2 (1 + e^(K(Vgb-Vto)-Vdb)/2Ut)
i = 0
thres = 0
for x in CcRaw:
    cVal = float(x)
    vVal = float(VgRaw[i])
    i+=1
    # if(i > 20):
    #     if(thres == 0):
    #         Cc.append(cVal)
    #         Vg.append(-1*vVal)
    #     thres+=1
    #     if(thres >0)
    #         thres = 0
    # else:
    Cc.append(-1*cVal)
    Vg.append(-1*vVal)

Vgtemp = []
Cctemp =[]
Cctemptemp =[]

count = 0
thres = 0
for m in reversed(Cc):
    # count+=1
    # if(count<30):
    #     if(thres ==2):
    #         Cctemp.append(m)
    #         thres = 0
    #     thres+=1
    # elif(count>32):
    Cctemp.append(m)

# i = len(Cctemp)-1
# for k in range(0,len(Cctemp)):
#     Cctemptemp.append(Cctemp[i])
#     i-=1
count = 0
thres = 0
for m in Vg:
    # count+=1
    # if(count<30):
    #     if(thres ==2):
    #         Vgtemp.append(m)
    #         thres = 0
    #     thres+=1
    # elif(count>32):
    Vgtemp.append(m)

Cctemp = np.array(Cctemp)
Vgtemp = np.array(Vgtemp)

end = len(Cctemp)
# plt.plot(Vgtemp[0:end],Cctemp[0:end], 'ro')
#
# plt.show()
# [Is, Vt, Kappa] = ekvfit(Vgtemp[0:end],Cctemp[0:end])

# print(Is)
# print(Vt)
# print(Kappa)

##runing ekv fit stops the code since I have it set to run plots, so here are the extracted values:
Is = 1.56109
Vt = -3.53489
Kappa = 0.3636

i = 0
for x in Cc:
    vVal = Vg[i]
    val = (Is * (math.log(1 + math.exp(Kappa*(vVal-float(Vt))/(2*0.0258))))**2)
    TheoCC.append(val/1e5)
    i+=1

Vg2 = Vg
Cc2 = Cc
TheoCC2 = TheoCC

if __name__ == '__main__':

    # Setting up plot
    title = "Collector Current as a function of gate voltage for an pMOS transistor"
    yLabel = "Collector Current (A)"
    xLabel = "Gate Voltage (V)"

    # Plotting Data

    Data1 = plt.semilogy(Vg, Cc, 'ro', markersize=3, label="experimental")
    Data2 = plt.semilogy(Vg[5:50], TheoCC[5:50], 'b--', markersize=3, label="EKV Model")

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.legend()
    plt.savefig('Exp1pMOS.png', format='png')
    plt.show()




#
