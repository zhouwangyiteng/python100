# _*_ coding: UTF-8 _*_

MAXIMUM = lambda x, y: (x>y) * x + (x<y) * y
MINIMUM = lambda x, y: (x<y) * x + (x>y) * y

a = 10
b = 20
print 'The larger one is %s.' % MAXIMUM(a, b)
print 'The lower one is %s.' % MINIMUM(a, b)
