# coding utf 8  -*-
a = int(input())
for i in range(a):
    name = 'пример-' + str(i + 1) + '.py'
    open(name, 'w+')
