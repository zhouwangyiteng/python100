# _*_ coding: UTF-8 _*_

for num in range(100, 1000):
    i = num / 100
    j = num % 10
    k = (num / 10) % 10
    if num == i**3 + j**3 + k**3:
        print num
