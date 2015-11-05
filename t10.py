# _*_ coding:UTF-8 _*_
import time

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

time.sleep(5)

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
