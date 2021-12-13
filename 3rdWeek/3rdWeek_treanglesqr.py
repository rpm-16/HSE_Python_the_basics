# Даны длины сторон треугольника. Вычислите площадь треугольника.
a, b, c = float(input()), float(input()), float(input())
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c))**0.5
if s % 1 == 0:
    print('{0:.0f}'.format(s))
else:
    print('{0:.6f}'.format(s))
