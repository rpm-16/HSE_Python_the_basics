# import time
# startTime = time.time()

# В олимпиаде участвовало N человек. Каждый получил определенное количество
# баллов, при этом оказалось, что у всех участников разное число баллов.
# Упорядочите список участников олимпиады в порядке убывания набранных баллов.

# Формат ввода
# Программа получает на вход число участников олимпиады N. Далее идет N строк,
# в каждой строке записана фамилия участника, затем, через пробел, набранное
# им количество баллов.

# Формат вывода
# Выведите список участников (только фамилии) в порядке убывания набранных
# баллов.

# input
countUsers = int(input())
# countUsers = int(3)
# users = [['Ivanov', '15'], ['Petrov', '10'], ['Sidorov', '20']]


users = []
# print(countUsers)

for i in range(countUsers):
    users.append(input().split())

# output
users.sort(key=lambda x: int(x[1]), reverse=True)
for user in users:
    print(user[0])

# totalTime = time.time() - startTime
# print("Время, затраченное на выполнение данного кода = ", totalTime)
