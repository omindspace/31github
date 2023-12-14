from decimal import *

getcontext().prec = int(input('Введите начальную точность:'))  # Десятичная точность.


def Factorial(F):
    result = 1
    for i in range(2, F + 1):
        result *= i
    return result


b = int(input('Введите число слагаемых:'))  # Число слагаемых.
n = 0
k = 0
while k <= b:
    getcontext().prec += 20 # Увеличивается точность.
    n += (Decimal(Factorial(4 * k) / (Factorial(k) ** Decimal(4))) * Decimal(
        (1103 + 26390 * k) / (Decimal((4 * 99) ** Decimal(4 * k)))))
    k += 1
N = n
n = Decimal(9801) / (Decimal(Decimal(2 * (Decimal(2 ** Decimal(0.5))) * N)))
print(Decimal(n))
input()
