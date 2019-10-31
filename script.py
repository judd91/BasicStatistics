# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
import pandas as pd
import numpy as np
from scipy import stats

filedata = open("text.txt", "r")
cont = 0
for line in filedata:
    if(cont == 0):
        n = int(line)
    else:
        numbers = line
    cont = cont + 1
    
data = numbers.split(" ")
data = map(int, data)
confidence = 1.96
l = len(data)

mean_sol = np.mean(data) 
median_sol = np.median(data)
mode_sol = stats.mode(data)
SD_sol = np.std(data)
ci = stats.norm.interval(0.950004, loc=mean_sol, scale=SD_sol/np.sqrt(n))
start = str("{0:.1f}".format(ci[0]))
end = str("{0:.1f}".format(ci[1]))

print"{0:.1f}".format(mean_sol)
print(median_sol)
print(mode_sol[0][0])
print "{0:.1f}".format(SD_sol)
print (start + " " + end) 
