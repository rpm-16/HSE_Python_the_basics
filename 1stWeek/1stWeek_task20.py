# Электронные часы показывают время в формате h:mm:ss, то есть
# сначала записывается количество часов (число от 0 до 23), потом
# обязательно двузначное количество минут, затем обязательно
# двузначное количество секунд. Количество минут и секунд при
# необходимости дополняются до двузначного числа нулями.

moment1h = int(input())
moment1m = int(input())
moment1s = int(input())
moment2h = int(input())
moment2m = int(input())
moment2s = int(input())

print((moment2h * 3600 + moment2m * 60 + moment2s) -(moment1h * 3600 + moment1m * 60 + moment1s))
