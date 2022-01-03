# import time
# startTime = time.time()

# В выборах Президента Российской Федерации побеждает кандидат, набравший
# свыше половины числа голосов избирателей. Если такого кандидата нет, то
# во второй тур выборов выходят два кандидата, набравших наибольшее число
# голосов.

# Формат ввода
# Каждая строка входного файла содержит имя кандидата, за которого отдал
# голос один избиратель. Известно, что общее число кандидатов не превосходит
# 20, но в отличии от предыдущих задач список кандидатов явно не задан.
# Читайте данные из файла input.txt с указанием кодировки utf8.

# Формат вывода
# Если есть кандидат, набравший более 50% голосов, программа должна вывести
# его имя. Если такого кандидата нет, программа должна вывести имя кандидата,
# занявшего первое место, затем имя кандидата, занявшего второе место.
# Выводите данные в файл output.txt с указанием кодировки utf8.

fileIn = open('input.txt', 'r', encoding='utf8')
applicantList = []
for line in fileIn:
    applicantList.append(line.rstrip())

countDict = {}
for applicant in applicantList:
    countDict[applicant] = countDict.get(applicant, 0) + 1
# print(countDict)

summ = 0
for k, v in countDict.items():
    summ += v
listm = [(k, v, v/summ*100) for k, v in countDict.items()]
listm = sorted(listm, key=lambda n: n[2], reverse=True)
# print(listm)


def get_vinners(arr):
    for item in arr:
        if item[2] > 50:
            return listm[0][0]
    return str(listm[0][0] + '\n' + listm[1][0])


fileout = open('output.txt', 'w', encoding='utf8')
print(get_vinners(listm), file=fileout)
fileIn.close()
fileout.close()

# totalTime = time.time() - startTime
# print("Время, затраченное на выполнение данного кода = ", totalTime)
