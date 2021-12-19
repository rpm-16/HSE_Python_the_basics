# Даны два целых числа A и B (при этом A≤B). Выведите все
# числа от A до B включительно.

a, b = int(input()), int(input())

for i in tuple(range(a, b + 1)):
    print(i, end=" ")
