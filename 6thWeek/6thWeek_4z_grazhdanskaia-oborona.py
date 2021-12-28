# import time
# startTime = time.time()

# В первой строке вводится число n - количество селений (1 <= n <= 100000).
# Вторая строка содержит n различных целых чисел, i-е из этих чисел задает
# расстояние от начала дороги до i-го селения. В третьей строке входных
# данных задается число m - количество бомбоубежищ (1 <= m <= 100000).
# Четвертая строка содержит m различных целых чисел, i-е из этих чисел
# задает расстояние от начала дороги до i-го бомбоубежища. Все расстояния
# положительны и не превышают 10⁹. Селение и убежище могут располагаться
# в одной точке.

# Формат вывода
# Выведите  n чисел - для каждого селения выведите номер ближайшего к нему
# бомбоубежища. Бомбоубежища пронумерованы от 1 до m в том порядке, в котором
# они заданы во входных данных.

# input
nVillages = int(input())  # (1 <= m <= 100000)
villageDistance = list(map(int, input().split()))
nBshelters = int(input())  # (1 <= m <= 100000)
bshelterDistance = list(map(int, input().split()))


def makeListTuples(Arr):
    for i in range(len(Arr)):
        Arr[i] = [i + 1, Arr[i]]
    Arr.sort(key=lambda Arr: Arr[1])
    return Arr


def findClosestShelter(vil):
    if vil > Shelters[-1][1]:
        return Shelters[-1][0]

    if vil < Shelters[0][1]:
        return Shelters[0][0]

    # Бинарный поиск
    firstSheltId = 0
    lastSheltId = len(Shelters) - 1

    while (lastSheltId - firstSheltId) > 1:
        mid = (firstSheltId + lastSheltId) // 2

        if vil > Shelters[mid][1]:
            firstSheltId = mid
        else:
            lastSheltId = mid

    if vil - Shelters[firstSheltId][1] < Shelters[lastSheltId][1] - vil:
        return Shelters[firstSheltId][0]
    else:
        return Shelters[lastSheltId][0]
    

Shelters = makeListTuples(bshelterDistance)

# output
output = []
for i in villageDistance:
    output.append(findClosestShelter(i))
print(*output)

# totalTime = time.time() - startTime
# print("Время, затраченное на выполнение данного кода = ", totalTime)
