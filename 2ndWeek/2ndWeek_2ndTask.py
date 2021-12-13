# Даны два целых числа. Программа должна вывести число "1", если
# первое число больше второго, число "2", если второе больше
# первого или число "0", если они равны.

number1 = int(input())
number2 = int(input())

if number1 > number2:
    print('1')
elif number1 < number2:
    print('2')
else:
    print('0')
