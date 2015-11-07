# _*_ coding: UTF-8 _*_

import sys



for i in range(4):
    for j in range(3-i):
        sys.stdout.softspace = 0
        print ' ',
    for j in range(2*i+1):
        sys.stdout.softspace = 0
        print '*',
    for j in range(3-i):
        sys.stdout.softspace = 0
        print ' ',
    print 
for i in [2,1,0]:
    for j in range(3-i):
        sys.stdout.softspace = 0
        print ' ',
    for j in range(2*i+1):
        sys.stdout.softspace = 0
        print '*',
    for j in range(3-i):
        sys.stdout.softspace = 0
        print ' ',
    print 
