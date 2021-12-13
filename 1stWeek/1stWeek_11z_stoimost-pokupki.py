# Задача "Стоимость покупки"
# Пирожок в столовой стоит A рублей и B копеек. Определите,
# сколько рублей и копеек нужно заплатить за N пирожков.

costRubs = int(input())
costPens = int(input())
countPies = int(input())
totalCostPens = (costRubs*100 + costPens) * countPies
print(totalCostPens // 100, totalCostPens % 100)
