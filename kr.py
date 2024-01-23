import math

# 5 Вариант
def strangeBullshit(a: int) -> int:
    amount = 0
    for i in range(1, n + 1):
        amount += int(math.pow(i, 3))
    return amount

n = int(input('Введите натуральное число N: '))
if n <= 0:
    print('N должно быть натуральным числом')
else:
    print('Сумма 1^3+.....n^3: ', strangeBullshit(n))
