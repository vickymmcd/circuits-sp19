
from scipy import stats
import math
import matplotlib.pyplot as plt
import numpy as np


# Exp 1 Data
Exp1_Ib = open('../exp1/Ib.txt', 'r').read().split()
Exp1_Ie = open('../exp1/Ie.txt', 'r').read().split()
Exp1_Vb = open('../exp1/Vb.txt', 'r').read().split()
linear_v = []
linear_i = []

V_bVals = []
I_cVals = []

alpha = 1;
beta = 100;

i = 0
for x in Exp1_Ib:
    I_bval = float(x)
    I_eval = float(Exp1_Ie[i])
    V_bval = float(Exp1_Vb[i])
    if V_bval > .4 and V_bval < .75:
        linear_v.append(V_bval)
        linear_i.append(np.log(float((-1*I_eval) - I_bval)))
    V_bVals.append(V_bval)
    I_cVals.append((-1*I_eval) - I_bval)
    i = i+1

slope, intercept, r_value, p_value, std_err = stats.linregress(linear_v, linear_i)

U_t = (1/(slope))
I_s = np.exp(intercept)


if __name__ == '__main__':
    Data = plt.semilogy(V_bVals, I_cVals, 'bo', markersize=3, label="300 Ohm Resistor")

    print(U_t)
    print(I_s)
    plt.show()
