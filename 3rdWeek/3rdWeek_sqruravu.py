# Квадратное уравнение - 1
# Даны действительные коэффициенты a, b, c, при этом a != 0. Решите квадратное
# уравнение ax²+bx+c=0 и выведите все его корни.

# Формат ввода
# Вводятся три действительных числа.

a, b, c = float(input()), float(input()), float(input())

D = b**2 - 4 * a * c

# roots
x1 = (-b + D**0.5) / (2 * a)
x2 = (-b - D**0.5) / (2 * a)
if D > 0:
    if x1 > x2:
        print(x2, x1)
    if x1 < x2:
        print(x1, x2)
if D == 0:
    print(x1)
