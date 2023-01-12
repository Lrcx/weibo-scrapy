import math

import pandas as pd

filename = '%23女权%23'

df=pd.read_csv(filename+'.csv',header=0)

negative,positive,middle,sum=0,0,0,0

for data in df.itertuples(index=False):
    score = data[-1]
    if math.isnan(score):
        continue
    sum+=score
    if score<=0.2:
        negative+=1
    elif score>0.6:
        positive+=1
    else:
        middle+=1


print(negative)
print(positive)
print(middle)

print(sum)
print(sum/len(df))