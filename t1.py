# _*_ coding: UTF-8 _*_

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j)and(i != k)and(j != k):
                print i, j, k
