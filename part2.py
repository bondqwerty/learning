#Цикл while
a = 1

while a < 10: #цикл будет работать пока это условие выполняется
    print('Цикл выполнился', a, 'раз(а)') #входим в цикл и совершается первое действие
    a = a+1 #второе действие в цикле, дальше идем опят на while
print('Цикл окончен') #действие после выхода из цикла

#break / continue 
i = 0
while i < 5:
    a, b = input().split()
    a = int(a)
    b = int(b)
    if (a==0) and (b==0) 
        break #досрочно завершаем цикл
    if (a==0) or (b==0) 
        continue #переходим к следующей итерации
    print(a*b)
    i+=1
    

#символы и строки
genome = 'ATGG'
genome[0[='A'
genome[-1]='G'

i=1
print(genome[i]) #T
 
#строки неизменяем, нельзя присвоить новый символ

#перечисление символов строки         
genome = 'ATGG'
for i in genome:
         print(i) #выдаст все символы с новой строки
         
#методы у строк
s='aTGcc'
g='cc'

s.upper #ATGCC
s.lower #atgcc
s.count(p) #сколько раз подстрока p встречается в строке s
s.find(p)
s.find('A') #строка A не входит в S
s.replace('c', 'C') #заменяем маленькое c на большое C

#можно использовать несколько вызовов функции
s='AkjfD'
s.upper().count('ak'.upper())  #результат 2    


#slicind
dna='ATGGCTCG'   
dna[1:4] #TGG
dna[-4:] #CTCG
dna[1:-1:2] #идем с шагом 2/TGTC
dna[::-1] #символы в обратном порядке
