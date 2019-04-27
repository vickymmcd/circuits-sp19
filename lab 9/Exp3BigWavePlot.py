
import numpy as np
import math
import csv
import matplotlib.pyplot as plt
from scipy import stats
from numpy import *

# Importing Data

timeBig = []

VoutBig = []

with open('RunforLargeWaveLab9.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        if len(row) == 1:
            row = row[0].split(",")
            firstval = float(row[0])
            secondval = float(row[1])
            thirdval = float(row[2])
            # print(firstval,"ee", secondval, thirdval)
            timeBig.append(firstval)
            VoutBig.append(thirdval)
#
# slope, intercept, r_value, p_value, std_err = stats.linregress(linearvdm, linearvout)
# linearvdm = np.array(linearvdm)

# #
# print(VoutBig[0])
# print(timeBig)
# Setting up plot
title = "Unity-Gain Follower Step Response"
yLabel = "Vout"
xLabel = "time"
#
Data1 = plt.plot(timeBig, VoutBig, 'ro', markersize=3)
# Data = plt.plot(linearvdm, (slope*linearvdm)+intercept, 'b', label="best fit line: y="+str(round(slope,5))+"x + " +str(round(intercept,5)))

plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.savefig('BigWave.png', format='png')
plt.show()
