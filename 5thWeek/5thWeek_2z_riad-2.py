# Даны два целых числа A и В. Выведите все числа от A до B
# включительно, в порядке возрастания,
# если A < B, или в порядке убывания в противном случае.

a, b = int(input()), int(input())
if a < b:
    for i in tuple(range(a, b + 1)):
        print(i, end=" ")
else:
    for i in tuple(range(a, b - 1, -1)):
        print(i, end=" ")
