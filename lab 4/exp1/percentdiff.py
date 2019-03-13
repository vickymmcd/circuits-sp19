import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import stats
import matplotlib.ticker as plticker
from one.trans1 import I_cVals1,Exp1_Vb
from two.trans2 import I_cVals2
from three.trans3 import I_cVals3
from four.trans4 import I_cVals4
mean=[]
pd1=[]
pd2=[]
pd3=[]
pd4=[]
Exp1_Vb1=[]
I_cVals11=[]
I_cVals21=[]
I_cVals31=[]
I_cVals41=[]
for x in Exp1_Vb:
    y = float(x)
    Exp1_Vb1.append(y)
for x in I_cVals1:
    y = float(x)
    I_cVals11.append(y)
for x in I_cVals2:
    y = float(x)
    I_cVals21.append(y)
for x in I_cVals3:
    y = float(x)
    I_cVals31.append(y)
for x in I_cVals4:
    y = float(x)
    I_cVals41.append(y)

for i in range(0,len(I_cVals11)):
    avg=(I_cVals11[i]+I_cVals21[i]+I_cVals31[i]+I_cVals41[i])
    avg1=avg*.25
    mean.append(avg1)
for k in range(0,len(I_cVals21)):
    pd=((I_cVals21[k]-mean[k])/mean[k])*100
    pd2.append(pd)
for k in range(0,len(I_cVals31)):
    pd=((I_cVals31[k]-mean[k])/mean[k])*100
    pd3.append(pd)
for k in range(0,len(I_cVals41)):
    pd=((I_cVals41[k]-mean[k])/mean[k])*100
    pd4.append(pd)
for k in range(0,len(I_cVals11)):
    pd=((I_cVals11[k]-mean[k])/mean[k])*100
    pd1.append(pd)

if __name__ == '__main__':
    plt.figure(0)
    title = "Percent Difference- Ic per transistor and mean of all Ics"
    xLabel = "Base Voltage (V)"
    yLabel = "Percent Difference"
    Data = plt.plot(Exp1_Vb1 , pd1, 'bo', markersize=3, label="Q1 Ic percent difference")
    Data = plt.plot(Exp1_Vb1 ,pd2,  'ro', markersize=3, label="Q2 Ic percent difference")
    Data = plt.plot(Exp1_Vb1, pd3 , 'go', markersize=3, label="Q3 Ic percent difference")
    Data = plt.plot( Exp1_Vb1 ,pd4, 'ko', markersize=3, label="Q4 Ic percent difference")

    plt.legend()
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    # plt.yticks(np.arange(0,10,step=.1))
    loc = plticker.MultipleLocator(base=10) # this locator puts ticks at regular intervals
    plt.grid(True)
    plt.show()
