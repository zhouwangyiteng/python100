# _*_ coding: UTF-8 _*_

from math import sqrt

total = 0
for i in range(101, 201):
    flag = 1
    k = int(sqrt(i))+1
    for j in range(2, k):
        if i % j == 0:
            flag = 0
            break
    if flag:
        total += 1
        print i

print "The total is %s" % total
    
