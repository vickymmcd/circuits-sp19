
from scipy import stats
import math
import matplotlib.pyplot as plt
import numpy as np

# Exp 1 Data
Exp1_Ib = open('exp1/Ib.txt', 'r').read().split()
Exp1_Ie = open('exp1/Ie.txt', 'r').read().split()
Exp1_Vb = open('exp1/Vb.txt', 'r').read().split()
linear_v = []
linear_i = []
beta_vals = []

V_bVals = []
I_cVals = []

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
    Exp1_Ib[i] = I_bval
    #beta_vals.append(((-1*I_eval) - I_bval)/I_bval)
    i = i+1

slope, intercept, r_value, p_value, std_err = stats.linregress(linear_v, linear_i)

U_t = (1/(slope))
I_s = np.exp(intercept)

i = 0
for x in Exp1_Ib:
    x = float(x)
    beta = (I_s/x)*np.exp(V_bVals[i]/U_t)
    beta_vals.append(beta)
    i+=1

beta = np.mean(beta_vals)


if __name__ == '__main__':
    #Data = plt.semilogy(V_bVals, I_cVals, 'bo', markersize=3, label="Ic values")
    #Data = plt.semilogy(V_bVals, Exp1_Ib, 'ro', markersize=3, label="Ib values")
    Data = plt.semilogx(Exp1_Ib, beta_vals, 'ro', markersize=3)

    print(U_t)
    print(I_s)
    print(beta)
    plt.legend()
    plt.show()




#
