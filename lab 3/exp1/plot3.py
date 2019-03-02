import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import stats
import matplotlib.ticker as plticker

Exp1_Ib = open('../exp1/Ib.txt', 'r').read().split()
Exp1_Ie = open('../exp1/Ie.txt', 'r').read().split()
Exp1_Vb = open('../exp1/Vb.txt', 'r').read().split()
i = 0
Exp1_Ic_Theo = []
Exp1_Ic = []
Exp1_Ib_Theo = []
rb=[]
exp1_ib2 = []

for x in Exp1_Ib:
    I_bval = float(x)
    I_eval = float(Exp1_Ie[i])
    Exp1_Ib[i] = I_bval
    Exp1_Ie[i] = I_eval
    Exp1_Vb[i] = float(Exp1_Vb[i])
    Exp1_Ic.append((-1*I_eval) - I_bval)
    i = i+1

for y in range(1,len(Exp1_Vb)):
    incv=Exp1_Vb[y]-Exp1_Vb[y-1]
    #print (Exp1_Ib[y])
    #print (Exp1_Ib[y-1])
    inci=Exp1_Ib[y]-Exp1_Ib[y-1]

    #print (incv)
    #print (inci)
    if inci != 0:
        rb.append(incv/inci)
        exp1_ib2.append(Exp1_Ib[y])

if __name__ == '__main__':

   title = "Rb versus Ib"
   xLabel = "Incremental Base Resistance (Ohms)"
   yLabel = "Base Current (A)"
   Data = plt.loglog(rb, exp1_ib2 , 'ko', markersize=3)
   plt.legend()
   plt.xlabel(xLabel)
   plt.ylabel(yLabel)
   plt.title(title)
   loc = plticker.MultipleLocator(base=100) # this locator puts ticks at regular intervals
   plt.grid(True)
   plt.show()
