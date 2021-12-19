# import time
# В первой строке задается одно натуральное число N, не превосходящее
# 1000 – размер массива.  Во второй строке содержатся N чисел – элементы
# массива (целые числа, не превосходящие по модулю 1000).  В третьей
# строке вводится одно целое число x, не превосходящее по модулю 1000.
# startTime = time.time()

N = int(input())
Na = list(map(int, input().split()))
x = int(input())

min = Na[0]
for i in Na:
    if abs(i - x) < abs(min - x):
        min = i
print(min)

# totalTime = time.time() - startTime
# print("Время, затраченное на выполнение данного кода = ", totalTime)
