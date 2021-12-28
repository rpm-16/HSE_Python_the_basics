# import time
# startTime = time.time()

# Для поступления в вуз абитуриент должен предъявить результаты трех экзаменов
# в виде ЕГЭ, каждый из них оценивается целым числом от 0 до 100 баллов. При
# этом абитуриенты, набравшие менее 40 баллов (неудовлетворительную оценку)
# по любому экзамену из конкурса выбывают. Остальные абитуриенты участвуют в
# конкурсе по сумме баллов за три экзамена.

# В конкурсе участвует N человек, при этом количество мест равно K. Определите
# проходной балл, то есть такое количество баллов, что количество участников,
# набравших столько или больше баллов не превосходит K, а при добавлении к ним
# абитуриентов, набравших наибольшее количество баллов среди непринятых
# абитуриентов, общее число принятых абитуриентов станет больше K.

# input
fileUsers = open('input.txt', 'r', encoding='utf8')
output = open('output.txt', 'w', encoding='utf8')
budgetplaces = int(fileUsers.readline())

scoreList = []
for line in fileUsers:
    line = line.rstrip().split()
    if int(line[-1]) >= 40 and int(line[-2]) >= 40 and int(line[-3]) >= 40:
        scoreList.append(int(line[-1]) + int(line[-2]) + int(line[-3]))
scoreList.sort(reverse=True)


def bbalform(budgetplaces, scoreList):
    if len(scoreList) <= budgetplaces:
        return 0

    elif scoreList.count(max(scoreList)) > budgetplaces:
        return 1

    else:
        for i in scoreList[:budgetplaces + 1]:
            if i > scoreList[budgetplaces]:
                tmp = i
        return tmp

# output
print(bbalform(budgetplaces, scoreList), file=output)
# print(bbalform(budgetplaces, scoreList))
# totalTime = time.time() - startTime
# print("Время, затраченное на выполнение данного кода = ", totalTime)
