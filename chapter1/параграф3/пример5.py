from graph import *
print("Введите координаты x и y и сторону квадрата")
x = int(input("x="))
y = int(input("y="))
a = int(input("Сторона ="))
rectangle(x, y, x+a, y+a)
run()