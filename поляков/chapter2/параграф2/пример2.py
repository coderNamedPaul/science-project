a = int(input())


def square():
    global a
    for i in range(a):
        if i == 0:
            print(' ', end='')
            print('--'*a)
        elif i == a-1:
            print(' ', end='')
            print('--'*a)
        else:
            print('|', ' '*(a*2), '|', sep='')


square()
