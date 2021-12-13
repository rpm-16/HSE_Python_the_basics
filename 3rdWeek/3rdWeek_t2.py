# По данному числу n вычислите сумму (1 / 1²)+(1 / 2²)+(1 / 3²)+...+(1 / n²).
n = float(input())
i, summ = 1, 0
while i <= n:
    summ += (1 / i**2)
    i += 1
print('{0:6f}'.format(summ))
