# Даны два натуральных числа n и m.
# Сократите дробь (n / m), то есть выведите два других числа p и q таких, что
# (n / m) = (p / q) и дробь (p / q) — несократимая.
# Решение оформите в виде функции ReduceFraction(n, m), получающая значения
# n и m и возвращающей кортеж из двух чисел: return p, q.
# Тогда вывод можно будет оформить как print(*ReduceFraction(n, m)).


def delit(n, m):
    global nod
# Алгоритм эвклида
    if n == 0 or m == 0:
        nod = int(n + m)
    else:
        if n > m:
            n = n % m
        else:
            m = m % n
        ReduceFraction(n, m)


def ReduceFraction(n, m):
    delit(n, m)
    p = int(n / nod)
    q = int(m / nod)
    return(p, q)

n, m = int(input()), int(input())
print(*ReduceFraction(n, m))
