Жители страны Малевии часто экспериментируют с планировкой комнат. 
Комнаты бывают треугольные, прямоугольные и круглые. Чтобы быстро 
вычислять жилплощадь, требуется написать программу, на вход которой 
подаётся тип фигуры комнаты и соответствующие параметры, которая бы выводила площадь получившейся комнаты.
Для числа π в стране Малевии используют значение 3.14.

Формат ввода, который используют Малевийцы:

треугольник
a
b
c

где a, b и c — длины сторон треугольника

прямоугольник
a
b

где a и b — длины сторон прямоугольника

круг
r

где r — радиус окружности


f = str (input())
if f == "прямоугольник":
    a = float (input())
    b = float (input())
    print (a*b)
elif f == "круг":
    r = float (input())
    print ((r**2)*3.14)
elif f == "треугольник":
    a = float (input())
    b = float (input())
    c = float (input())
    p = (a+b+c)/2
    print ((p*(p-a)*(p-b)*(p-c))**(1/2))