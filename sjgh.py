import csv
f=open("SOCR-HeightWeight.csv")
file = csv.reader(f)
data=list(file)
data.pop(0)

height=[]
for i in range (0,len(data)):
    num=data[i][1]
    height.append(float(num))

sum=0
for i in height:
    sum=sum +i

mean=sum/len(height)
print(mean)

import statistics
print(statistics.mean(height))