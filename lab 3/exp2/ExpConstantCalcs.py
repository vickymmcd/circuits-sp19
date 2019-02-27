
from scipy import stats
import math
import matplotlib.pyplot as plt

# Exp 1 Data
Exp1_Ib = open('../exp1/Ib.txt', 'r').read().split()
Exp1_Ie = open('../exp1/Ie.txt', 'r').read().split()
Exp1_Vb = open('../exp1/Vb.txt', 'r').read().split()

V_bVals = []
I_cVals = []

i = 0
for x in Exp1_Ib:
    I_bval = float(x)
    I_eval = float(Exp1_Ie[i])
    V_bval = float(Exp1_Vb[i])
    V_bVals.append(V_bval)
    I_cVals.append((-1*I_eval) - I_bval)

    i = i+1






#
