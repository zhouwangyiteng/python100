# _*_ coding: UTF-8 _*_
import string

s = raw_input('Input a string:')
letters = 0
digit = 0
space = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print 'char = %d, space = %d, digit = %d, others = %d' % (letters, space, digit, others)
