# import time
# startTime = time.time()

# Дан список чисел, который может содержать до 100000 чисел.Определите,
# сколько в нем встречается различных чисел.

# input
numList = map(int, input().split())
# numList = map(int, '1 2 3 4 5 6 7 8 9 10'.split())

# output
print(len(set(numList)))


# totalTime = time.time() - startTime
# print("Время, затраченное на выполнение данного кода = ", totalTime)
