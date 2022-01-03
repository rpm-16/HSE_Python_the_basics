# import time
# startTime = time.time()

# Вам дан словарь, состоящий из пар слов. Каждое слово является
# синонимом к парному ему слову. Все слова в словаре различны. Для
# одного данного слова определите его синоним.

fileIn = open('input.txt', 'r', encoding='utf8')
nWords = int(fileIn.readline())
wordsList = {}
for i in range(nWords):
    w1 = fileIn.readline().strip().split()
    wordsList[w1[0]] = w1[1]
searchWord = fileIn.readline().strip()


def get_answer(dict, word):
    for key, value in dict.items():
        if value == word:
            return key
        if key == word:
            return value


print(get_answer(wordsList, searchWord))

# print(*wordsList[searchWord])

# totalTime = time.time() - startTime
# print("Время, затраченное на выполнение данного кода = ", totalTime)
