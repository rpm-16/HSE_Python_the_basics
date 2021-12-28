# import time
# startTime = time.time()


# Системный администратор вспомнил, что давно не делал архива
# пользовательских файлов. Однако, объем диска, куда он может
# поместить архив, может быть меньше чем суммарный объем
# архивируемых файлов.

# Известно, какой объем занимают файлы каждого пользователя.
# Напишите программу, которая по заданной информации о пользователях
# и свободному объему на архивном диске определит максимальное число
# пользователей, чьи данные можно поместить в архив.


Ssd, Users = list(map(int, (input().split())))
UserDataList = []

for i in range(Users):
    UserDataList.append(int(input()))
UserDataList.sort()

summ = 0
count = 0
for j in UserDataList:
    summ += j
    if summ >= Ssd:
        break
    count += 1

print(count)


# print(*UserDataList)
# for i in UserDataList:
#     print(UserDataList)


# totalTime = time.time() - startTime
# print("Время, затраченное на выполнение данного кода = ", totalTime)
