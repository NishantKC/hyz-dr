import csv 
import math

f = open("class1.csv")
file = csv.reader(f)
data = list(file)
data.pop(0)
Marks = []
for i in range(0,len(data)):
    num = data[i][1]
    Marks.append(int(num))

sum = 0
for i in Marks:
    sum = sum+i

mean = sum/len(Marks)
print(mean)

squares = []
for i in Marks: 
    a = int(i)-mean
    a = a**2
    squares.append(a)

sum = 0
for i in squares:
    sum = sum+i

result = sum/(len(Marks)-1)

div = math.sqrt(result)
print(div)

import statistics
print(statistics.stdev(Marks))