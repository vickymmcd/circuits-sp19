import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import stats
from consts import beta_vals
import matplotlib.ticker as plticker

Exp1_Ib = open('../exp1/Ib.txt', 'r').read().split()
Exp1_Ie = open('../exp1/Ie.txt', 'r').read().split()
Exp1_Vb = open('../exp1/Vb.txt', 'r').read().split()
i = 0
Exp1_Ic_Theo = []
Exp1_Ic = []
Exp1_Ib_Theo = []
beta=[]
for x in Exp1_Ib:
    I_bval = float(x)
    I_eval = float(Exp1_Ie[i])
    Exp1_Ib[i] = I_bval
    Exp1_Ie[i] = I_eval
    Exp1_Vb[i] = float(Exp1_Vb[i])
    Exp1_Ic.append((-1*I_eval) - I_bval)
    #print("appending")
    i = i+1
for h in range(0,len(Exp1_Ib)):
    beta.append(Exp1_Ic[h]/Exp1_Ib[h])

print(beta)
if __name__ == '__main__':


   plt.figure(0)
   title = "Current Gain"
   xLabel = "Base Current (A)"
   yLabel = "Current Gain"
   Data = plt.semilogx( Exp1_Ib,beta, 'ko', markersize=3, label="beta = Ic/Ib")
   Data = plt.semilogx( Exp1_Ib[:-3],beta_vals[:-3], 'ro', markersize=3, label="beta = Is/Ib * e^(Vb/Ut)")
   plt.legend()
   plt.xlabel(xLabel)
   plt.ylabel(yLabel)
   plt.title(title)
   loc = plticker.MultipleLocator(base=100) # this locator puts ticks at regular intervals
   plt.grid(True)
   plt.show()
