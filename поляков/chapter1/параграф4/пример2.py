from graph import *
x, y, R = map(int, input().split())
def circleIn (x, y, R):
    brushColor('brown')
    rectangle(x-R-20, y-R-20, x+R+20, y+R+20)
    brushColor('red')
    circle(x, y, R)

circleIn(x, y, R)
run()