import random
# Для данного числа n<100 закончите фразу “На лугу пасется...” 
# одним из возможных продолжений: “n коров”, “n корова”, “n коровы”,
# правильно склоняя слово “корова”.

cowCount = int(input())
cowCount = random.randint(1, 100)

ost = cowCount %10
if ost == 1:
    strCow='корова'
elif  4 >= ost >= 2:
    strCow='коровы'
elif  ost >= 5 or ost == 0:
    strCow='коров'
print('На лугу пасеться', cowCount, strCow)

