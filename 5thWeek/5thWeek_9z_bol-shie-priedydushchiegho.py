# Дан список чисел. Выведите все элементы списка, которые больше
# предыдущего элемента.


mList = list(map(int, input().split()))
i = 0
while i < len(mList)-1:
    if mList[i] < mList[i+1]:
        print(mList[i+1], end=' ')
    i += 1
