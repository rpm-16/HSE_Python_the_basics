# По российский правилам числа округляются до ближайшего целого
# числа,а если дробная часть числа равна 0.5, то число округляется
# вверх. Дано неотрицательное число x, округлите его по этим
# правилам. Обратите внимание, что функция round не годится
# для этой задачи!
n = float(input())
cel = n // 1
if n % 1 >= 0.5:
    dr = 1
else:
    dr = 0
print(int(cel + dr))
