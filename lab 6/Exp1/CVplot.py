
import sys
sys.path.append('..')
from ekvfit import ekvfit
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats
from numpy import *

from ExtractT1 import Is, Vt, Kappa
Is1 = Is
Vt1 = Vt
K1 = Kappa

from ExtractT2 import Is, Vt, Kappa
Is2 = Is
Vt2 = Vt
K2 = Kappa

from ExtractT3 import Is, Vt, Kappa
Is3 = Is
Vt3 = Vt
K3 = Kappa

from ExtractT4 import Is, Vt, Kappa
Is4 = Is
Vt4 = Vt
K4 = Kappa

# Importing Data
Id1Raw = open('T1/Id.txt', 'r').read().split() #Collector Current
Vg1Raw = open('T1/Vg.txt', 'r').read().split() #Gate Voltage

Id2Raw = open('T2/Id.txt', 'r').read().split() #Collector Current
Vg2Raw = open('T2/Vg.txt', 'r').read().split() #Gate Voltage

Id3Raw = open('T3/Id.txt', 'r').read().split() #Collector Current
Vg3Raw = open('T3/Vg.txt', 'r').read().split() #Gate Voltage

Id4Raw = open('T4/Id.txt', 'r').read().split() #Collector Current
Vg4Raw = open('T4/Vg.txt', 'r').read().split() #Gate Voltage

Id1 = []
Vg1 = []

Id2 = []
Vg2 = []

Id3 = []
Vg3 = []

Id4 = []
Vg4 = []

i = 0
for x in Id1Raw:
    Id1.append(float(x))
    Vg1.append(float(Vg1Raw[i]))

    Id2.append(float(Id2Raw[i]))
    Vg2.append(float(Vg2Raw[i]))

    Id3.append(float(Id3Raw[i]))
    Vg3.append(float(Vg3Raw[i]))

    Id4.append(float(Id4Raw[i]))
    Vg4.append(float(Vg4Raw[i]))
    i+=1

TheoI1 = []
TheoI2 = []
TheoI3 = []
TheoI4 = []

i = 0
for x in Id1:
    vVal = Vg1[i]
    TheoI1.append(Is1 * (math.log(1 + math.exp(K1*(vVal-float(Vt1))/(2*0.0258))))**2)
    TheoI2.append(Is2 * (math.log(1 + math.exp(K2*(vVal-float(Vt2))/(2*0.0258))))**2)
    TheoI3.append(Is3 * (math.log(1 + math.exp(K3*(vVal-float(Vt3))/(2*0.0258))))**2)
    TheoI4.append(Is4 * (math.log(1 + math.exp(K4*(vVal-float(Vt4))/(2*0.0258))))**2)
    i+=1


# Setting up plot
title = "Current Voltage Characteristics of ALD1106 Transistor Chip"
yLabel = "Drain Current (A)"
xLabel = "Gate Voltage (V)"

Data1 = plt.semilogy(Vg1, Id1, 'ro', markersize=3.5, label="T1")
Data2 = plt.semilogy(Vg2, Id2, 'ko', markersize=3, label="T2")
Data3 = plt.semilogy(Vg3, Id3, 'co', markersize=2.5, label="T3")
Data4 = plt.semilogy(Vg4, Id4, 'bo', markersize=2, label="T4")
start = 4
Data5 = plt.semilogy(Vg1[start:], TheoI1[start:], 'r--', markersize=3.5, label="T1 Fit")
Data6 = plt.semilogy(Vg2[start:], TheoI2[start:], 'k--', markersize=3, label="T2 Fit")
Data7 = plt.semilogy(Vg3[start:], TheoI3[start:], 'c--', markersize=2.5, label="T3 Fit")
Data8= plt.semilogy(Vg4[start:], TheoI4[start:], 'b--', markersize=2, label="T4 Fit")

plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.legend()
plt.savefig('Exp1CV.png', format='png')
plt.show()














    #
