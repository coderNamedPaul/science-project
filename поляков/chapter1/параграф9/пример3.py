#Операция 'НЕ' (not)
a = int(input("Введите число < или = 100 (целое): "))
if not(a <= 100):
    print("Число не подходит")
else:
    print("Число подходит")