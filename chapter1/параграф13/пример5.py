from graph import *

penColor("brown")
penSize(5)

x1 = 100
x2 = 300
y1 = 100
y2 = 200
rectangle(x1, y1, x2, y2)

N = 10
h = round((x2-x1)/N)

for x in range(x1+h, x2, h):
    penColor("black")
    line(x, y1, x, y2)

run()