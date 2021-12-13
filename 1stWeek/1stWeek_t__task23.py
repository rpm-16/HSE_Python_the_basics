# За день машина проезжает N километров. Сколько дней нужно, чтобы проехать
# маршрут длиной M километров?

oneDay = int(input())
oneWay = int(input())
print((oneWay + (oneDay - 1)) // oneDay)
