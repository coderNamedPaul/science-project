from graph import *  # размер доступной области : 500x600
def roof() :
    penColor('red')
    brushColor('red')
    polygon([(50, 80), (250, 10), (450, 80), (50, 80)])
def frame() :
    penColor(163, 99, 26)
    brushColor(163, 99, 26)
    rectangle(100, 81, 400, 380)
def windows () :
    penSize(5)
    penColor('grey')
    brushColor('yellow')
    circle(250, 45, 30)
    line(250, 12, 250, 75)
    line(220, 45, 280, 45)
    rectangle(110, 120, 220, 320)
    line(165, 120, 165, 320)
    line(110, 220, 220, 220)
def door ():
    penColor(77, 41, 0)
    brushColor(77, 41, 0)
    rectangle(240, 190, 360, 379)
roof()
frame()
windows()
door()
run()
