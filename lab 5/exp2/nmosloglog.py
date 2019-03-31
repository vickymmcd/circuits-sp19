import sys
sys.path.append('..')
from linefit import linefit
from ekvfit import ekvfit
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats
pIout = open('nmosexp2/Iout.txt', 'r').read().split()
pVin = open('nmosexp2/Vin.txt', 'r').read().split()
pI=[]
pV=[]
ppI=[]
ppV=[]
gsw=[]
gss=[]
gsp=[]
gwp=[]
ge=[]

i = 0
thres=0
ro=-1/.00045
for x in pIout:
    pI.append(float(x)*-1)
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

ge=-1*np.diff(pI)/np.diff(pV)
print(ge)
#Strong Inversion
for p in pI[6:]:
    va=ro*p
    gss.append(math.sqrt((.00005*p)/.0258))
    gsp.append(va/(.0258*ro)*math.sqrt(.00005/p))
#Weak Inversion
for i in pI[6:]:
    va=ro*i
    gsw.append(i/.0258)
    gwp.append(va/(.0258*ro))

title = "Current as a function of the Source Voltage in nMOS"
yLabel = "I_sat(amps)"
xLabel = "Incremental Source Conductance (gs) (mhos)"

[first, last, mmax, bmax, Nmax]=linefit(np.array(pV[6:]),np.array(pI[6:]))
x = np.logspace(.25,.55,2)
y = mmax*x+bmax
Data2=plt.loglog( pI[1:],ge, 'bo',label='Experimental')
Data2=plt.loglog( pI[6:],gss, '-m',label='Strong Inversion Region Fit')
Data2=plt.loglog( pI[6:],gsw, '-r',label='Weak Inversion Region Fit')
#Data2=plt.loglog(gsp, pI[6:], 'go')
#Data2=plt.loglog(gwp, pI[6:], 'mo')
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.legend()
plt.savefig('Exp2NMOSloglogreal.png', format='png')
plt.show()
labely = "y="+str(round(mmax,5))+"x+ "+str(round(bmax,5))
