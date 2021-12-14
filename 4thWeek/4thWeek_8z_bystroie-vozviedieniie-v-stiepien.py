# Возводить в степень можно гораздо быстрее, чем за n умножений! Для этого
# нужно воспользоваться следующими рекуррентными соотношениями: aⁿ = (a²)ⁿ/²
# при четном n, aⁿ=a⋅aⁿ⁻¹ при нечетном n. Реализуйте алгоритм быстрого
# возведения в степень. Если вы все сделаете правильно,то сложность вашего
# алгоритма будет O(logn).


def rec(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return rec(a**2, n / 2)
    else:
        return a * rec(a, n - 1)

a, n = float(input()), int(input())
print(rec(a, n))
