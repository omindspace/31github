n = int(input(' Введите 1 число :'))
m = int(input(' Введите 2 число :'))

if m == 0: print(' Нельзя делить на ноль!')

if m != 0:
    result = n / m
    
    print(n,'/',m,'=', result)
