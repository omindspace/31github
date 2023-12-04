n = int(input('Введите номер месяца:'))
if n == 12: print('Зима')
elif n == 1: print('Зима')
elif n == 2: print('Зима')
elif n == 3 or n == 4 or n == 5: print('Весна')
elif n >= 6 and n <= 8: print('Лето')
elif n in [9, 10, 11]: print('Осень')
else:
    print('Нет такого месяца!')
