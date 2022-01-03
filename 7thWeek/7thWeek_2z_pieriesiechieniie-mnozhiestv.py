# import time
# startTime = time.time()

# Во входной строке записана последовательность чисел через пробел.
# Для каждого числа выведите слово YES (в отдельной строке), если
# это число ранее встречалось в последовательности или NO, если
# не встречалось.

# input
print(*sorted(set(map(int, input().split())) & set(map(int, input().split()))))


# totalTime = time.time() - startTime
# print("Время, затраченное на выполнение данного кода = ", totalTime)
