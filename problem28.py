Напишите программу, которая подключает модуль math и, используя значение числа \piπ из этого модуля, 
находит для переданного ей на стандартный ввод радиуса круга периметр этого круга и выводит его на стандартный вывод.


import math

r = float(input())
per = 2.0*math.pi*r
print(per)
