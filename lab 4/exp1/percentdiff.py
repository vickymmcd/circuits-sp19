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
for i in range(0,len(I_cVals1)):
    avg=(I_cVals1[i]+I_cVals2[i]+I_cVals3[i]+I_cVals4[i])
    avg1=avg*.25
    mean.append(avg1)
for k in range(0,len(I_cVals2)):
    pd=(I_cVals2[k]-mean[k])/mean[k]
    pd2.append(pd)
for k in range(0,len(I_cVals3)):
    pd=(I_cVals3[k]-mean[k])/mean[k]
    pd3.append(pd)
for k in range(0,len(I_cVals4)):
    pd=(I_cVals4[k]-mean[k])/mean[k]
    pd4.append(pd)
for k in range(0,len(I_cVals1)):
    pd=(I_cVals1[k]-mean[k])/mean[k]
    pd1.append(pd)

if __name__ == '__main__':
    plt.figure(0)
    title = "Beta versus Ib"
    xLabel = "Beta"
    yLabel = "Base Current(A)"
    Data = plt.plot(Exp1_Vb , pd1, 'bo', markersize=3, label="Q1")
    Data = plt.plot(Exp1_Vb ,pd2,  'ro', markersize=3, label="Q2")
    Data = plt.plot(Exp1_Vb, pd3 , 'go', markersize=3, label="Q3")
    Data = plt.plot( Exp1_Vb ,pd4, 'ko', markersize=3, label="Q4")

    plt.legend()
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    # plt.yticks(np.arange(0,10,step=.1))
    loc = plticker.MultipleLocator(base=10) # this locator puts ticks at regular intervals
    plt.grid(True)
    plt.show()
