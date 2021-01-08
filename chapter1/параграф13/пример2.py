from graph import *

penColor("black")
brushColor("blue")
penSize(2)

for y in range(50, 151, 50):
    for x in range(50, 251, 50):
        circle(x, y, 20)
run()