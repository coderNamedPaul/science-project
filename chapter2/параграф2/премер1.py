def plus(a, b):
    print(a+b)


def minus(a, b):
    print(a-b)


action = input()
a, b = map(int, input().split())

if action == '-':
    minus(a, b)
elif action == '+':
    plus(a, b)
