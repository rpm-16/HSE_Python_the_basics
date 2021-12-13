# Даны три целых числа. Найдите наибольшее
# из них (программа должна вывести ровно одно целое число).
# Какое наименьшее число операторов сравнения (>, <, >=, <=)
# необходимо для решения этой задачи?

number1 = int(input())
number2 = int(input())
number3 = int(input())

if number1 >= number2 and number1 >= number3:
    print(number1)
elif number2 >= number1 and number2 >= number3:
    print(number2)
else:
    print(number3)
