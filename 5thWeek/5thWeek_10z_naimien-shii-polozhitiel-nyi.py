# Выведите значение наименьшего из всех положительных элементов в списке.
# Известно, что в списке есть хотя бы один положительный элемент, а
# значения всех элементов списка по модулю не превосходят 1000.

mList = list(map(int, input().split()))
min = 1000

for item in mList:
    if item > 0:
        if item <= min:
            min = item
print(min)
