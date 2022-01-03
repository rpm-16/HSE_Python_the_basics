# import time
# startTime = time.time()

# Во входной строке записана последовательность чисел через пробел.
# Для каждого числа выведите слово YES (в отдельной строке), если
# это число ранее встречалось в последовательности или NO, если
# не встречалось.

# input
listnumbers = list(map(int, input().split()))
plentynumbers = set()

for n in listnumbers:
    if n in plentynumbers:
        print('YES')
    else:
        print('NO')
        plentynumbers.add(n)

# totalTime = time.time() - startTime
# print("Время, затраченное на выполнение данного кода = ", totalTime)
