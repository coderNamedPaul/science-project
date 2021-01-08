from graph import *

penColor("black")
penSize(2)

def Romb(x, y):
    polygon([(x, y), (x+10, y-20), (x+20, y), (x+10, y+20), (x, y)])
for x in range(20, 61, 10):
    Romb(x, 30)
run()