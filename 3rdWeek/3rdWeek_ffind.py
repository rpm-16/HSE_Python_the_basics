# Дана строка. Если в этой строке буква f встречается только один раз, выведите
# её индекс. Если она встречается два и более раз, выведите индекс её первого и
# последнего появления. Если буква f в данной строке не встречается, ничего не
# выводите. При решении этой задачи нельзя использовать метод count и циклы.

str = str(input())
# str = "officer fucker"
pos = str.find('f')

if pos != -1:
    print(pos)
    pos = str.find('f', pos + 1)

if pos != -1:
    unstr = str[::-1]
    upos = unstr.find('f')
    print(len(str) - upos - 1)
