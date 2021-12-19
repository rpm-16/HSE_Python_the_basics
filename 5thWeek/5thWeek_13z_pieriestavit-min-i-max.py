# В списке все элементы попарно различны. Поменяйте местами минимальный
# и максимальный элемент этого списка.

mList = list(map(int, input().split()))
min = 1000

for item in mList:
    if item > 0:
        if item <= min:
            min = item
print(min)
