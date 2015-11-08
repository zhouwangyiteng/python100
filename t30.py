# _*_ coding: UTF-8 _*_

num = raw_input('Enter a number:')
length = len(num)
flag = 1
for i in range(length/2):
    if num[i]!=num[length-i-1]:
        flag = 0
if flag:
    print 'Yes'
else:
    print 'No'

    
