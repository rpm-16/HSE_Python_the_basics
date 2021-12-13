# Задача "Сумма цифр трехзначного числа"
# Дано трехзначное число. Найдите сумму его цифр.

userNum = int(input())
units = (userNum % 100) % 10
dozens = (userNum % 100) // 10
hundreds = userNum // 100

print(hundreds + dozens + units)
