Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, 
которые встречаются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.

Sample Input 1:
4 8 0 3 4 2 0 3

Sample Output 1:
0 3 4


a = [ int(i) for i in input().split()]
b=[]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            if a[i] not in b:
                b.append(a[i])
            break
        else:
            continue
for m in range(0,len(b)):
    print(b[m],end='')
    
