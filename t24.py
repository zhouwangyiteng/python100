# _*_ coding: UTF-8 _*_

a = 1.0
b = 2.0
s = 0
for i in range(20):
    s += b/a
    a, b = b, a+b
print s
