# import time
# startTime = time.time()

# Дан текст. Выведите слово, которое в этом тексте встречается
# чаще всего. Если таких слов несколько, выведите то, которое
# меньше в лексикографическом порядке.

fileIn = open('input.txt', 'r', encoding='utf8')
wordsList = []
for line in fileIn:
    line = line.rstrip().split()
    for word in line:
        wordsList.append(word)

countDict = {}
for word in wordsList:
    word = str(word)
    countDict[word] = countDict.get(word, 0) + 1
# countDict = {word: (countDict.get(word, 0) + 1) for word in wordsList}
max_val = max(countDict.values())

final_dict = {k: v for k, v in countDict.items() if v == max_val}
print(sorted(final_dict)[0])


# totalTime = time.time() - startTime
# print("Время, затраченное на выполнение данного кода = ", totalTime)
