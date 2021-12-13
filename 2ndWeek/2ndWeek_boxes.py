# Есть две коробки, первая размером A₁×B₁×C₁, вторая размером A₂×B₂×C₂.
# Определите, можно ли разместить одну из этих коробок внутри другой,
# при условии, что поворачивать коробки можно только на 90 градусов
# вокруг ребер.

# a1, b1, c1 = int(input()), int(input()), int(input())
# a2, b2, c2 = int(input()), int(input()), int(input())

a1, b1, c1 = 1, 2, 3
a2, b2, c2 = 3, 2, 1


if ((a1 == a2 and b1 == b2 and c1 == c2) or
    (a1 == b2 and b1 == c2 and c1 == a2) or
    (a1 == c2 and b1 == a2 and c1 == b2) or
    (a1 == c2 and b1 == a2 and c1 == b2)
    ):
    print('Boxes are equal')
    
#@ print('The first box is smaller than the second one,')
# если первая коробка может быть положена во вторую,

# print('The first box is larger than the second one')
# если вторая коробка может быть положена в первую,

else:
    print('Boxes are incomparable'), 
# во всех остальных случаях.