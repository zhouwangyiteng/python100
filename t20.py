# _*_ coding: UTF-8 _*_

s = 100.0
h = s / 2
n=10
for i in range(n-1):
    s += 2*h
    h = h/2
print s
print h
