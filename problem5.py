Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа.

a = int (input())
b = int (input())
c = int (input())

if a>=b and b<=c and a<=c:
    print(c)
    print(b)
    print(a)
elif a>=b and a>=c and b<=c:
    print(a)
    print(b)
    print(c)
elif a>=b and a>=c and b>=c:
    print(a)
    print(c)
    print(b)
elif a<=b and a<=c and b<=c:
    print(c)
    print(a)
    print(b)
elif a<=b and a<=c and b>=c:
    print(b)
    print(a)
    print(c)
elif a<=b and a>=c and b>=c:
    print(b)
    print(c)
    print(a)
