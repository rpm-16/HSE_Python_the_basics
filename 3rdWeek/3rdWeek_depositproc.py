import math
# Процентная ставка по вкладу составляет P процентов годовых,
# которые прибавляются к сумме вклада. Вклад составляет
# X рублей Y копеек. Определите размер вклада через год.
# При решении этой задачи нельзя пользоваться условными
# инструкциями и циклами.
P, X, Y = int(input()), int(input()), float(input())
depositInPens = X * 100 + Y
SummDepoEnd = depositInPens/100 * P + depositInPens

print(int(SummDepoEnd // 100), int(SummDepoEnd % 100))
