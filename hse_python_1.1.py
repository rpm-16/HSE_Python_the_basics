# Первый урок типы данных и функции вывода
""""Это многострочный комментарий в пайтон
по сути это анонимный обьъект"""

name = "Pavel"
print(f"My name is {name}")
print("Hello world"+" 2")
print('2 + 3 =', 2+3)
print('1', '2', '3', sep=' + ', end=' ') 
#sep - разделитель имноованный параментр функиции принт
#end - пустая строка для отмены перевола каретки на новую строку

"""В качестве параметра sep можно использовать любую строку, в том числе
состоящую из нескольких символов. Если нам нужно сделать несколько 
разных разделителей для разных частей строк, то не остается другого
выбора, кроме как использовать несколько подряд идущих функций print.
Например, если мы хотим вывести строку вида 1 + 2 + 3 + 4 = 10, то можем
попробовать воспользоваться следующим кодом:"""
print(1, 2, 3, 4, sep=' + ', end='')
print(' = ', 1 + 2 + 3 + 4, sep='')   
