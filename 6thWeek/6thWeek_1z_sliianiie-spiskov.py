# import time
# startTime = time.time()
# Даны два целочисленных списка A и B, упорядоченных по неубыванию.
# # Объедините их в один упорядоченный список С (то есть он должен
# содержать len(A)+len(B) элементов). Решение оформите в виде функции
# merge(A, B), возвращающей новый список. Алгоритм должен иметь
# сложность O(len(A)+len(B)). Модифицировать исходные списки
# запрещается. Использовать функцию sorted и метод sort запрещается.

A, B = list(map(int, input().split())), list(map(int, input().split()))
C = []


def merge(A, B):

    # Просто хрень
    i, j, C = 0, 0, []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    C += A[i:]
    C += B[j:]
    return C

print(*merge(A, B))

# totalTime = time.time() - startTime
# print("Время, затраченное на выполнение данного кода = ", totalTime)
