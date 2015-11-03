# _*_ coding:UTF-8 _*_
import datetime

year = int(raw_input('year:'))
month = int(raw_input('month:'))
day = int(raw_input('day:'))

oneday = datetime.date(year, month, day)
print (oneday - datetime.date(year, 1, 1)).days + 1
