# _*_ coding: UTF-8 _*_

n = int(raw_input('input n:'))
a1 = 1
a2 = 1
for i in range(1, n):
    a1, a2 = a2, a1 + a2
print a1
