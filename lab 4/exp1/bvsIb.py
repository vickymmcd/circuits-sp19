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


if __name__ == '__main__':
    plt.figure(0)
    title = "Beta versus Ib"
    xLabel = "Beta"
    yLabel = "Base Current(A)"
    Data = plt.semilogx(Exp1_Ib ,beta1, 'bo', markersize=3, label="Q1")
    Data = plt.semilogx(Exp2_Ib , beta2,'ro', markersize=3, label="Q2")
    Data = plt.semilogx(Exp3_Ib , beta3,'go', markersize=3, label="Q3")
    Data = plt.semilogx(Exp4_Ib , beta4,'ko', markersize=3, label="Q4")

    plt.legend()
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    loc = plticker.MultipleLocator(base=100) # this locator puts ticks at regular intervals
    plt.grid(True)
    plt.show()
