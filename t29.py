# _*_ coding: UTF-8 _*_

num = raw_input('Enter a number:')
print 'The length of the number is', len(num)
num = int(num)
while(num>0):
    print num%10
    num /= 10

    
