import sys
sys.path.append('..')
from linefit import linefit
from ekvfit import ekvfit
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats
pIout = open('pmosexp2/Iout.txt', 'r').read().split()
pVin = open('pmosexp2/Vin.txt', 'r').read().split()
pI=[]
pV=[]
ppI=[]
ppV=[]
i = 0
thres=0
for x in pIout:
    pI.append(float(x)*1)
    pV.append(float(pVin[i]))
    i+=1
    if(i>20):
        if(thres==4):
            ppI.append(pI)
            ppV.append(pV)
        thres+=1
        if (thres>4):
            thres=0
    else:
        ppI.append(pI)
        ppV.append(pV)

[Is,Ut,Kappa]=ekvfit(np.array(pV),np.array(pI))
#Strong Inversion
#gs=sqrt(Is*Isat)/Ut



#Weak Inversion
#gs=Isat/Ut
title = "Current as a function of the Source Voltage in nMOS"
yLabel = "Current"
xLabel = "Source Voltage"

[first, last, mmax, bmax, Nmax]=linefit(np.array(pV[6:]),np.array(pI[6:]))
x = np.logspace(.25,.55,2)
y = mmax*x+bmax
Data2=plt.loglog(gs, pI, '-r','ro')
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.legend()
plt.savefig('Exp2nMOSlog.png', format='png')
plt.show()
labely = "y="+str(round(mmax,5))+"x+ "+str(round(bmax,5))
