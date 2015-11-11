# _*_ coding: UTF-8 _*_

from Tkinter import *

canvas = Canvas(width=400, height=300, bg='green')
canvas.pack(expand=YES, fill=BOTH)

k = 1
j = 5
for i in range(0, 10):
    canvas.create_oval(210-k, 150-k, 210+k, 150+k, width=1)
    k += j
    j += 1.5

mainloop()
