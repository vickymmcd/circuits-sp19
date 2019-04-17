import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import stats
import matplotlib.ticker as plticker
from one.trans1 import I_s1, beta1
from two.trans2 import I_s2, beta2
from three.trans3 import I_s3, beta3
from four.trans4 import I_s4, beta4
Exp1_Ib = open('one/Ib.txt', 'r').read().split()
Exp2_Ib = open('two/Ib.txt', 'r').read().split()
Exp3_Ib = open('three/Ib.txt', 'r').read().split()
Exp4_Ib = open('four/Ib.txt', 'r').read().split()

Ib1 = []
Ib2 = []
Ib3 = []
Ib4 = []


i = 0
for x in Exp1_Ib:
    I_bVal = float(x)
    if(i == 6):
        Ib1.append(-1.6e-10)
    else:
        Ib1.append(I_bVal)
    i+=1

for x in Exp2_Ib:
    I_bVal = float(x)
    Ib2.append(I_bVal)


for x in Exp3_Ib:
    I_bVal = float(x)
    Ib3.append(I_bVal)


for x in Exp4_Ib:
    I_bVal = float(x)
    Ib4.append(I_bVal)

if __name__ == '__main__':
    plt.figure(0)
    title = "Beta versus Ib"
    xLabel = "Beta"
    yLabel = "Base Current(A)"
    Data = plt.semilogx(Ib1 , beta1, 'bo', markersize=3, label="Q1")
    Data = plt.semilogx(Ib2 , beta2,'ro', markersize=3, label="Q2")
    Data = plt.semilogx(Ib3 , beta3,'go', markersize=3, label="Q3")
    Data = plt.semilogx(Ib4 , beta4,'ko', markersize=3, label="Q4")

    plt.legend()
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    loc = plticker.MultipleLocator(base=100) # this locator puts ticks at regular intervals
    plt.grid(True)
    plt.ylim((-100,20000))
    plt.savefig('BataVIb.png', format='png')
    plt.show()
