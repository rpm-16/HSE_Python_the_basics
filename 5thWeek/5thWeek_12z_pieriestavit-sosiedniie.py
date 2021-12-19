# Переставьте соседние элементы списка (A[0] c A[1],A[2] c A[3]
# и т.д.).Если элементов нечетное число, то последний элемент
# остается на своем месте.

A = list(map(int, input().split()))
lenA = len(A)
if lenA % 2 != 0:
    lenA -= 1
# print(lenA)

i = 0
while i < lenA:
    (A[i], A[i + 1]) = (A[i + 1], A[i])
    i += 2
print(*A)
