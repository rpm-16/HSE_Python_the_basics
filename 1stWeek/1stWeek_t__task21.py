# ЭДаны два момента времени в пределах одних и тех же суток.
# Для каждого момента указан час, минута и секунда. Известно,
# что второй момент времени наступил не раньше первого.
# Определите сколько секунд прошло между двумя моментами времени.

secondsGone = int(input())
daysLeft = secondsGone // 86400
# print(3600 * 24)
hoursLeft = (secondsGone % 86400) // 3600
print(hoursLeft, ':', sep='', end='')

minutesLeft = (secondsGone % 3600) // 60
print(minutesLeft // 10, minutesLeft % 10, ':', sep='', end='')

secondsLeft = (secondsGone % 60)
print(secondsLeft // 10, secondsLeft % 10, sep='')
