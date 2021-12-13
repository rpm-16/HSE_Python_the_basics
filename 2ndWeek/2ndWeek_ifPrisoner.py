# import random
# За многие годы заточения узник замка Иф проделал в стене
# прямоугольное отверстие размером D×E. Замок Иф сложен из
# кирпичей, размером A×B×C. Определите, сможет ли узник
# выбрасывать кирпичи в море через это отверстие (очевидно,
# стороны кирпича должны быть параллельны сторонам отверстия).

a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())

# a, b, c = random.randint(1, 5),random.randint(1, 5),random.randint(1, 5)
# d, e = random.randint(1, 5), random.randint(1, 5)

# print('brick', a, b, c)
# print('pitch', d, e)

if a <= d and b <= e or b <= d and a <= e:
    print('YES')
elif b <= d and c <= e or c <= d and b <= e:
    print('YES')
elif a <= d and c <= e or c <= d and a <= e:
    print('YES')
else:
    print('NO')
