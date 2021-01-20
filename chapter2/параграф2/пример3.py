from math import sqrt
while True:
    b =input()

    if b == 'exit':
        break
    else:
        b = int(b)


    def haveASquare(value):
        valueSTR = str(sqrt(value))
        index = valueSTR.index('.')
        r = valueSTR[index:]
        if len(r) > 2:
            return False
        else:
            return True, sqrt(value)


    print(haveASquare(b))
