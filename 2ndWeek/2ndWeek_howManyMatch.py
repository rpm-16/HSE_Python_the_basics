# import random
# Даны три целых числа. Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел: 3 (если все совпадают), 2
# (если два совпадает) или 0 (если все числа различны).

a, b, c = int(input()), int(input()), int(input())
# a, b, c = random.randint(1, 5),random.randint(1, 5),random.randint(1, 5)
countMatch = 0
if a == b or a == c or b == c:
    countMatch = 2

if a == b == c:
    countMatch = 3

print(countMatch)
