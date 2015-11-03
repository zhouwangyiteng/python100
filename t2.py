# _*_ coding: UTF-8 _*_

gain = int(raw_input("Input gain:"))

bonus1 = 100000 * 0.1
bonus2 = bonus1 + 100000 * 0.075
bonus4 = bonus2 + 200000 * 0.05
bonus6 = bonus4 + 200000 * 0.03
bonus10 = bonus6 + 400000 * 0.015

if gain <= 100000:
    bonus = gain * 0.1
elif gain <=200000:
    bonus = bonus1 + (gain - 100000) * 0.075
elif gain <=400000:
    bonus = bonus2 + (gain - 200000) * 0.05
elif gain <=600000:
    bonus = bonus4 + (gain - 400000) * 0.03
elif gain <=1000000:
    bonus = bonus6 + (gain - 600000) * 0.015
else:
    bonus = bonus10 + (gain - 1000000) * 0.01

print 'bonus=',  bonus
    
