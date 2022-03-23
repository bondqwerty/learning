На ввод даются два числа, на вывод сумма нечетных чисел в их промежутке.

a = int(input())
b = int(input())
sum=0
for i in range(a,b+1):
    if (i%2==1):
        sum+=i
print(sum)
