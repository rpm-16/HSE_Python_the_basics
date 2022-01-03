# import time
# startTime = time.time()
# Во входном файле (вы можете читать данные из sys.stdin, подключив
# библиотеку sys) записан текст. Словом считается последовательность
# непробельных символов идущих подряд, слова разделены одним или
# большим числом пробелов или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.

# input
fileIn = open('input.txt', 'r', encoding='utf8')
plenty = set()
for line in fileIn:
    for i in line.rstrip().split():
        plenty.add(i)
print(len(plenty))

# totalTime = time.time() - startTime
# print("Время, затраченное на выполнение данного кода = ", totalTime)
