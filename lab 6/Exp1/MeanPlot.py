
import sys
sys.path.append('..')
from ekvfit import ekvfit
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats
from numpy import *


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

diff1 = []
diff2 = []
diff3 = []
diff4 = []

MeanVal = []

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

    MeanVal.append((float(x) + float(Id2Raw[i]) + float(Id3Raw[i]) + float(Id4Raw[i]))/4)
    i+=1

i = 0
for x in Id1:
    diff1.append(abs(x-MeanVal[i])/(((x+MeanVal[i])/2))*100)
    diff2.append(abs(Id2[i]-MeanVal[i])/(((x+MeanVal[i])/2))*100)
    diff3.append(abs(Id3[i]-MeanVal[i])/(((x+MeanVal[i])/2))*100)
    diff4.append(abs(Id4[i]-MeanVal[i])/(((x+MeanVal[i])/2))*100)
    i+=1


# Setting up plot
title = "Percent Difference and Mean Value of Collector Current"
yLabel = "Channel Current Percent Difference (%Diff of A)"
xLabel = "Mean Channel Current (A)"

# Data1 = plt.semilogx(MeanVal, MeanVal, 'ro', markersize=3, label="Mean Current Value")
Data2 = plt.semilogx(MeanVal, diff1, 'ko', markersize=3, label="T1 Percent Difference")
Data3 = plt.semilogx(MeanVal, diff2, 'bo', markersize=3, label="T2 Percent Difference")
Data4 = plt.semilogx(MeanVal, diff3, 'co', markersize=3, label="T3 Percent Difference")
Data5 = plt.semilogx(MeanVal, diff4, 'yo', markersize=3, label="T4 Percent Difference")


plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.legend()
plt.savefig('ExpMeanGraph.png', format='png')
plt.show()






    #
