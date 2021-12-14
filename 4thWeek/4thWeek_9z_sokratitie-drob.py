# Даны два натуральных числа n и m.
# Сократите дробь (n / m), то есть выведите два других числа p и q таких, что
# (n / m) = (p / q) и дробь (p / q) — несократимая.
# Решение оформите в виде функции ReduceFraction(n, m), получающая значения
# n и m и возвращающей кортеж из двух чисел: return p, q.
# Тогда вывод можно будет оформить как print(*ReduceFraction(n, m)).


def ReduceFraction(n, m):
    x = n
    while x >= 1:
        if n % x == 0 and m % x == 0:
            return int(n / x), int(m / x)
        x -= 1


n, m = int(input()), int(input())
print(*ReduceFraction(n, m))
