# Дано натуральное число n>1. Выведите его наименьший делитель,
# отличный от 1. Решение оформите в виде функции MinDivisor(n).
# Алгоритм должен иметь сложность# порядка корня квадратного из n.

# Указание. Если у числа n нет делителя не превосходящего корня из n,
# то число n — простое и ответом будет само число n. А у всех
# составных чисел обязательно есть делители, отличные от единицы и
# не превосходящие корня из n.


def MinDivisor(n):
    x = 2
    while x <= n**0.5:
        if n % x == 0:
            return x
        x += 1
    else:
        return n

n = int(input())
print(MinDivisor(n))