import random
# Шахматный король ходит по горизонтали, вертикали и диагонали,
# но только на 1 клетку. Даны две различные клетки шахматной
# доски, определите, может ли король попасть с первой клетки на
# вторую одним ходом.

Point1x = int(input())
Point1y = int(input())
# print('Point 1:', startPointx, startPointx)

Point2x = int(input())
Point2y = int(input())
# print('Point 2:', startPointy, startPointy)

if Point1x - 1 <= Point2x <= Point1x + 1 and Point1y - 1 <= Point2y <= Point1y + 1:
        print('YES')
else:
    print('NO')
