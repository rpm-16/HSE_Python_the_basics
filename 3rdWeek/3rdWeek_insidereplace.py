# Дана строка. Замените в этой строке все появления буквы h на букву H,
# кроме первого и последнего вхождения.
str = str(input())
# str = 'In the hole in the ground there lived a hobbit'
nums = str.count('h')
if nums > 2:
    pos = str.find('h')
    print(str[0:pos+1], end='')
    print(str[pos+1:].replace('h', 'H', nums-2))
else:
    print(str)

# i = 2
# while i < pos:
#     str2 = str.replace('h', 'H')
#     i += 1
# print(str2)
