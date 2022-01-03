# import time
# startTime = time.time()

# Во входном файле (вы можете читать данные из файла input.txt)
# записан текст. Словом считается последовательность непробельных
# подряд идущих символов. Слова разделены одним или большим
# числом пробелов или символами конца строки. Для каждого
# слова из этого текста подсчитайте, сколько раз оно встречалось
# в этом тексте ранее.

fileIn = open('input.txt', 'r', encoding='utf8')
wordsList = []
for line in fileIn:
    for i in line.rstrip().split():
        wordsList.append(i)

countDict = {}
for word in wordsList:
    print(countDict.get(word, 0), end=' ')
    countDict[word] = countDict.get(word, 0) + 1

# totalTime = time.time() - startTime
# print("Время, затраченное на выполнение данного кода = ", totalTime)
