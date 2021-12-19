# Выведите все четные элементы списка.


mList = list(map(int, input().split()))
i = 0
while i < len(mList):
    if mList[i] % 2 == 0:
        print(mList[i], ' ', end='')
    i += 1
