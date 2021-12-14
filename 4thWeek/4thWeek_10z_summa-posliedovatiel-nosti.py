# Дана последовательность чисел, завершающаяся числом 0. Найдите
# сумму всех этих чисел, не используя цикл.


def sumMy():
    n = int(input())
    if n == 0:
        return 0
    else:
        return int(n + sumMy())

print(sumMy())
