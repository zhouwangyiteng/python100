# _*_ coding: UTF-8 _*_

def quickSort(a, l, r):
    if l>=r:
        return
    i = l
    j = r
    key = a[(l+r)/2]
    while i<j:
        while i<j and a[j]>=key:
            j -= 1
        if i<j:
            a[i] = a[j]
            i += 1
        while i<j and a[i]<key:
            i += 1
        if i<j:
            a[j] = a[i]
            j -= 1
    a[i] = key
    quickSort(a, l, i-1)
    quickSort(a, i+1, r)

b = [1,2,1,2,5,4,3,7,5,8,6,4,2,34,5,245,45,6547,345,29]
print b
quickSort(b, 0, len(b)-1)
print b
