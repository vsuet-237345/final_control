import math

# 3 Вариант
def strangeBullshit(a: int, b: int):
    if b >= a:
        print('A должно быть больше B')
        return

    print('Нечётные числа:')
    for i in range(b, a):
        if math.fmod(i, 2):
            print(i)

a = int(input('Введите число A: '))
b = int(input('Введите число B: '))

strangeBullshit(a, b)
