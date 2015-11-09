# _*_ coding: UTF-8 _*_

a = []
n = int(raw_input('Enter n:'))
for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(float(raw_input('Input a[%s][%s]:' %(i, j))))

for i in range(n):
    print '[',
    for j in range(n):
        print a[i][j],
    print ']'

total = 0
for i in range(n):
    total += a[i][i]

print total
