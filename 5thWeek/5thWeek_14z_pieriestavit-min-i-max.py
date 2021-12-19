# В списке все элементы попарно различны. Поменяйте местами минимальный
# и максимальный элемент этого списка.

A = list(map(int, input().split()))
min = A.index(min(A))
max = A.index(max(A))
(A[min], A[max]) = (A[max], A[min])
print(*A)
# print(min, max)
