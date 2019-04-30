
import numpy as np
import math
import csv
import matplotlib.pyplot as plt
from scipy import stats
from numpy import *

# Importing Data

timeBig = []

VoutBig = []

stepBig = []

with open('RunforLargeWaveLab9.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        if len(row) == 1:
            row = row[0].split(",")
            firstval = float(row[0])
            secondval = float(row[1])
            thirdval = float(row[2])
            timeBig.append(firstval)
            VoutBig.append(thirdval)
            stepBig.append(secondval)


peaktopeak = max(VoutBig)-min(VoutBig)
print(peaktopeak)

VoutBigSub1 = VoutBig[0:1500]
max = 0
maxIn = 0
i = 0
timeStartDecend = 0
timeEndDecend = 0

for x in VoutBigSub1:
    if(x > max):
        max = x
        maxin = i
    i+=1

timeStartDecend = -0.0243465
timeEndDecend = -0.018695
slewDownRate = timeStartDecend- timeEndDecend
print(slewDownRate)

timeStartAccend = -0.0143897
timeEndAccend = -0.000624492
slewUpRate = timeStartAccend- timeEndAccend
print(slewUpRate)

title = "Unity-Gain Follower Step Response"
yLabel = "Vout (Volts)"
xLabel = "time (seconds)"


Data1 = plt.plot(timeBig, VoutBig, 'ro', markersize=3)
Data2 = plt.plot(timeBig, stepBig, 'bo', markersize=3)
# Data = plt.plot(linearvdm, (slope*linearvdm)+intercept, 'b', label="best fit line: y="+str(round(slope,5))+"x + " +str(round(intercept,5)))

plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(title)
plt.savefig('BigWave.png', format='png')
plt.show()
