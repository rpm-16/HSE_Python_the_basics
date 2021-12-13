# Квадратное уравнение - 1
# Даны вещественные числа a, b, c, d, e, f. Известно, что система
# линейных уравнений:
# ax + by = e
# cx + dy = f
# имеет ровно одно решение. Выведите два числа x и y, являющиеся
# решением этой системы.

a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())

# методом Крамера
# Основной определитель
osnOp = a * d - c * b
vspmOp1 = e * d - f * b
vspmOp2 = a * f - c * e
# print(osnOp, vspmOp1, vspmOp2)
x = vspmOp1 / osnOp
y = vspmOp2 / osnOp
print(x, y)
