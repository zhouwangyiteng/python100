# _*_ coding: UTF-8 _*_

a = int(raw_input('Input a:'))
n = int(raw_input('Input n:'))
t = a
s = 0
for i in range(n):
    s += a
    a += t * 10
print s
