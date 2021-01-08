from graph import *

penColor("black")
brushColor("blue")
penSize(2)

def Row(y):
    for x in range(70, 351, 70):
        circle(x, y, 30)
for y in range(70, 211, 70):
    Row(y)

run()