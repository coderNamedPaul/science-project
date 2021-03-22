from graph import *

penColor("brown")
penSize(5)

x1 = 100
x2 = 300
y1 = 100
y2 = 200
rectangle(x1, y1, x2, y2)

N = 9
h = (x2-x1)/N
x = x1 + h

while x < x2:
    penColor("black")
    line(round(x), y1, round(x), y2)
    x += h
run()
