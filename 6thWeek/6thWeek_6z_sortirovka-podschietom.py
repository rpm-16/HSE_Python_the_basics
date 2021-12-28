# import time
# startTime = time.time()

# Дан список из N (N≤2*10⁵) элементов, которые принимают
# целые значения от 0 до 100 (100 включая).

# Отсортируйте этот список в порядке неубывания элементов.
# Выведите полученный список.

# Решение оформите в виде функции CountSort(A), которая
# модифицирует передаваемый ей список. Использовать
# встроенные функции сортировки нельзя.

# input
inlist = input()
# inlist = '9 8 7 6 5 4 3 2 1 0'


def CountSort(inData):
    arr = map(int, inData.split())
    tmpList = [0] * 101

    for item in arr:
        tmpList[item] += 1

    for i in range(101):
        print((str(i) + ' ') * tmpList[i], end='')


CountSort(inlist)
# totalTime = time.time() - startTime
# print("Время, затраченное на выполнение данного кода = ", totalTime)
