
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
IdRaw = open('T4/Id.txt', 'r').read().split() #Collector Current
VgRaw = open('T4/Vg.txt', 'r').read().split() #Gate Voltage

Id = []
Vg = []


i = 0
for x in IdRaw:
    Id.append(float(x))
    Vg.append(float(VgRaw[i]))
    i+=1



[Is, Vt, Kappa] = ekvfit(np.array(Vg[4:]), np.array(Id[4:]))

if __name__ == "__main__":
    print("Is = ")
    print(Is)
    print("Vt = ")
    print(Vt)
    print("K =")
    print(Kappa)


#
