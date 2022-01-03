# import time
# startTime = time.time()

# Каждый из N школьников некоторой школы знает Mᵢ языков. Определите, какие
# языки знают все школьники и языки, которые знает хотя бы один из
# школьников.

# Формат ввода
# Первая строка входных данных содержит количество школьников N. Далее идет
# N чисел Mᵢ, после каждого из чисел идет Mᵢ строк, содержащих названия
# языков, которые знает i-й школьник. Длина названий языков не превышает
# 1000 символов, количество различных языков не более 1000. 1≤N≤1000,
# 1≤Mᵢ≤500.

# Формат вывода
# В первой строке выведите количество языков, которые знают все школьники.
# Начиная со второй строки - список таких языков. Затем - количество
# языков, которые знает хотя бы один школьник, на следующих строках
# - список таких языков.

# input
fileIn = open('input.txt', 'r', encoding='utf8')
N = int(fileIn.readline().rstrip())
lang = []
for i in fileIn:
    sch = set()
    for x in range(int(i)):
        sch.add(fileIn.readline().rstrip())
    lang.append(sch)

all = set()
for i in range(len(lang)):
    all |= lang[i]

allknow = all.copy()
for i in range(len(lang)):
    allknow &= lang[i]

print(len(allknow), *sorted(allknow, reverse=True), sep='\n')
print(len(all), *sorted(all, reverse=True), sep='\n')

# totalTime = time.time() - startTime
# print("Время, затраченное на выполнение данного кода = ", totalTime)
