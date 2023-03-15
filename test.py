from math import ceil, floor
p = int(input())
x = int(input())
y = int(input())
time = 1
y1 = x * 100 + y
p = (p/100) * time
pyear = y1 * p
totsum = (y1 + pyear) / 100
x1 = int(totsum)
y2= round(totsum-x1,3)*100
print (x1, int(y2))