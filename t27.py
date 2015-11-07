# _*_ coding: UTF-8 _*_

def reShow(s):
    if len(s)==1:
        print s
        return ''
    reShow(s[1:])
    print s[0]
    return ''

print reShow('abcdef')
