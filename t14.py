# _*_ coding: UTF-8 _*_
import math

def isNotPrime(num):
    k = int(math.sqrt(num)) + 1
    for i in range(2, k):
        if num%i == 0:
            return True
    return False

n = int(raw_input('Input n:'))
print n, '=',
result = []
t = 2
while(n!=1):
    while(n%t==0):
        n /= t
        result.append(t)
    t += 1
    while(isNotPrime(t)):
        t += 1
print result[0],
for i in result[1:]:
    print '*', i,
    
