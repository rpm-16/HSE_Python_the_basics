# Задача "Вторая справа цифра"
# Дано натуральное число. Найдите цифру, стоящую в разряде
# десятков в его десятичной записи (вторую справа цифру или
# 0, если число меньше 10).

numb = int(input())
print((numb % 100) // 10)
