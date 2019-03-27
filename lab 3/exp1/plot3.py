import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import stats
import matplotlib.ticker as plticker
from plot1 import Exp1_Ib_Theo,Exp1_Ic_Theo
from plot4 import gm_theo,exp1_ib2
from consts import U_t
Exp1_Ib = open('../exp1/Ib.txt', 'r').read().split()
Exp1_Ie = open('../exp1/Ie.txt', 'r').read().split()
Exp1_Vb = open('../exp1/Vb.txt', 'r').read().split()
i = 0
#Exp1_Ic_Theo = []
Exp1_Ic = []
exp2=[]
#Exp1_Ib_Theo = []
rbtheo=0
rb=[]
Theorb = []
exp1_ib2 = []
logedExp1_Ib = []
logedrb = []
gm = []
gmTheo = []

for x in Exp1_Ib:
    I_bval = float(x)
    I_eval = float(Exp1_Ie[i])
    Exp1_Ib[i] = I_bval
    Exp1_Ie[i] = I_eval
    Exp1_Vb[i] = float(Exp1_Vb[i])
    Exp1_Ic.append((-1*I_eval) - I_bval)
    rb.append(0.025/I_bval)
    gm.append((-1*I_eval) - I_bval/0.025)

    i = i+1


# for y in range(1,len(Exp1_Vb)):
#     incv=Exp1_Vb[y]-Exp1_Vb[y-1]
#     #print (Exp1_Ib[y])
#     #print (Exp1_Ib[y-1])
#     inci=Exp1_Ib[y]-Exp1_Ib[y-1]
#
#     #print (incv)
#     #print (inci)
#     if inci != 0:
#         rb.append(incv/inci)
#         exp1_ib2.append(Exp1_Ib[y])
# slope, intercept, r_value, p_value, std_err = stats.linregress(Exp1_Ib,rb)
#
# for x in Exp1_Ib:
#    rbTheo.append(x*slope + intercept)

slope, intercept, r_value, p_value, std_err = stats.linregress(Exp1_Vb,Exp1_Ic)
U_t = (1/slope)
for x in Exp1_Vb:
     Exp1_Ib_Theo.append(2e-17*math.exp(x/0.025))
     Theorb.append(0.025/(2.5e-17*math.exp(x/0.025)))
     gmTheo.append((2.5e-17*math.exp(x/0.025))/0.025)


if __name__ == '__main__':

   title = "Gm versus Ic"
   xLabel = "Incremental Transconductance Gain (S)"
   yLabel = "Collector Current (A)"
   # Data = plt.loglog(Exp1_Ib , rb, 'ko', markersize=3)
   # plt.loglog(Exp1_Ib  , Theorb , 'r', markersize=3)
   plt.loglog(Exp1_Ic, gm, 'ko', markersize=3)
   plt.loglog(Exp1_Ic, gmTheo, 'r', markersize=3)
   plt.legend()
   plt.ylabel(xLabel)
   plt.xlabel(yLabel)
   plt.title(title)
   loc = plticker.MultipleLocator(base=100) # this locator puts ticks at regular intervals
   plt.grid(True)
   plt.show()
