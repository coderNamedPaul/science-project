from random import randint
score = 0


def game():
    global score
    rightAnswer = randint(1, 10)
    question = rightAnswer**2
    print('корень из', question)
    userAnswer = input()

    if userAnswer == 'exit':
        return 0
    elif userAnswer == 'score':
        print('твой счет:', score)
    elif userAnswer.isdigit():
        userAnswer = int(userAnswer)
        if userAnswer == rightAnswer:
            score += 1
            print('+1')
        else:
            score -= 1
            print(-1)
    game()


game()
