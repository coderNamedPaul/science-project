from graph import *

def update():
    global x
    x += 5
    moveObjectBy(obj, 5, 0)
    if x >= 400 - R: close()

brushColor("blue")
rectangle(0, 0, 400, 400)

R = 10
y = 200
x = 10
penColor("yellow")
brushColor("yellow")
obj = circle(x, y, R)

def keyPressed(event):
    if event.keycode == VK_ESCAPE:
        close()

onTimer(update, 32)

onKey(keyPressed)

run()