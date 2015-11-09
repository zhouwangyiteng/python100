# _*_ coding: UTF-8 _*_

from math import sqrt

def isPrimeNumber(n):
    if n<=1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

for i in range(100):
    if isPrimeNumber(i):
        print i
