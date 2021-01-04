print('загадайте играбельную рассу из starcraft и бот ее отгодает')  # отвечать только да или нет
answer = input('это расса гуманоидов?\n')
if answer == 'да':
    answer == input('их создали Зел-нага?\n')
    if answer == 'да':
        print('это расса протосов')
    elif answer == 'нет':
        print('это расса теранов')
elif answer == 'нет':
    print('это расса зергов')
