# Дана строка, в которой буква h встречается минимум два раза.Удалите из этой
# строки первое и последнее вхождение буквы h,а также все символы, находящиеся
# между ними.

str = str(input())
# str = "In the hole in the ground there lived a hobbit"
pos = str.find('h')

if pos != -1:
    # print(pos)
    # pos = str.find('h', pos + 1)
    print(str[0:pos], end='')

if pos != -1:
    unstr = str[::-1]
    upos = unstr.find('h')
    pos2 = len(str) - upos
    print(str[pos2:])
