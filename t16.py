# _*_ coding: UTF-8 _*_
import datetime

print datetime.date.today().strftime('%d/%m/%Y')

birthDate = datetime.date(1995, 3, 2)
print birthDate.strftime("%Y-%m-%d")

birthNextDate = birthDate + datetime.timedelta(days=1)

print birthNextDate.strftime("%Y-%m-%d")

firstBirthday = birthDate.replace(year=birthDate.year+21)

print firstBirthday.strftime("%Y-%m-%d")
