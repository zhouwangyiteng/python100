# _*_ coding: UTF-8 _*_

from Tkinter import *

canvas = Canvas(width=300, height=300, bg='green')
canvas.pack(expand=YES, fill=BOTH)

x0 = 263
y0 = 263
y1 = 275

for i in range(19):
    canvas.create_line(x0, y0, x0, y1, width=1, fill='red')
    x0 -= 5
    y0 -= 5
    y1 += 5

x0 = 263
y0 = 263
y1 = 275
for i in range(21):
    canvas.create_line(x0, y0, x0, y1, fill='red')
    x0 += 5
    y0 += 5
    y1 += 5
    
mainloop()
