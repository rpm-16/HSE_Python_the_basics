PenguinsCount = int(input())
PImg1 = '   _~_    '
PImg2 = '  (o o)   '
PImg3 = ' /  V  \  '
PImg4 = '/(  _  )\ '
PImg5 = '  ^^ ^^   '

print(PImg1 * PenguinsCount)
print(PImg2 * PenguinsCount)
print(PImg3 * PenguinsCount)
print(PImg4 * PenguinsCount)
print(PImg5 * PenguinsCount)


#Task description
# Напишите программу, которая по данному числу N от 1 до 9 
# выводит на экран N пингвинов. Изображение одного пингвина
# имеет размер 5×9 символов, между двумя соседними пингвинами 
# также имеется пустой (из пробелов) столбец. Разрешается вывести 
# пустой столбец после последнего пингвина. Для упрощения рисования
# скопируйте пингвина из примера в среду разработки.

#Requirements
#TimeLimit: 1000ms
#RamSizeLimit: 65536kb
    
#PenguinImage
#    _~_    
#   (o o)   
#  /  V  \  
# /(  _  )\ 
#   ^^ ^^