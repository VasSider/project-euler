import pandas as pd
import math

#p099_base_exp.txt
data = pd.read_csv("p099_base_exp.txt", sep=",", header=None) 

max_data = data[1].loc[0]*math.log10(data[0].loc[0])
ls=[0]
for i in range(0,len(data)):
    if max_data < data[1].loc[i]*math.log10(data[0].loc[i]):
        max_data = data[1].loc[i]*math.log10(data[0].loc[i])
        ls.append(i)

print (ls[-1])
