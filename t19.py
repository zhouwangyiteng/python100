# _*_ coding: UTF-8 _*_


for n in range(1, 1000):
    total = 0
    for i in range(1, n):
        if n%i == 0:
            total += i
    if total==n:
        print n

