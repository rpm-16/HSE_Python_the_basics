# считываем файл построчно, первая строка - количество мест,
# остальные строки - берем последние 3 значения, преобразуем в число,
# если все больше 40, то создаем список с суммарным значением


def getList():
    result = []

    with open('input.txt', 'r', encoding='utf8') as f:
        k = int(f.readline())

        for line in f:
            score = list(map(int, line.rstrip().split()[-3::]))
            if min(score) >= 40:
                result.append(sum(score))
    return result, k


# обрабатываем полученный список
# если мест хватает на всех, то выводим ноль
# если не определить проходной балл, то выводим 1
# в остальных случаях выводим проходной балл


def processList(lst, k):
    outFile = open('output.txt', 'w', encoding='utf8')

    if len(lst) <= k:
        print(0, file=outFile)
    else:
        lst.sort(reverse=True)
        answer = 1
        for now in lst[:k + 1]:
            if now > lst[k]:
                answer = now
        print(answer, file=outFile)


processList(*getList())