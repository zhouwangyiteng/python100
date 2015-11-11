# _*_ coding: UTF-8 _*_

from Tkinter import *

root = Tk()
root.title('Canvas')
canvas = Canvas(root, width=300, height=300, bg='green')
canvas.pack(expand=YES, fill=BOTH)

x0 = 145
y0 = 145
x1 = 155
y1 = 155
for i in range(10):
    canvas.create_rectangle(x0, y0, x1, y1)
    x0 -= 10
    y0 -= 10
    x1 += 10
    y1 += 10

    
root.mainloop()
