# Найдите количество положительных элементов в данном списке.


mList = list(map(int, input().split()))
i, count = 0, 0
while i < len(mList):
    if mList[i] > 0:
        count += 1
    i += 1
print(count)
