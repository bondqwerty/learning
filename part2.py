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


#списки
students= ['Masha','Sasha', 'Grisha']
for student in students:
         print('Hello'+student+'!')

len(students) #3
students[0] #Masha
students[-1] #Grisha

#операции со списками

#сложение
students= ['Masha','Sasha', 'Grisha']
teachers= ['Tolya']

students+teachers #Masha, Sasha, Grisha, Tolya

#умножение
[0,1]*4 #[0,1,0,1,0,1,0,1]
         
#изменение списков (списки можно изменять, а не перезаписывать элементы, как это было с другими типами переменных)
students= ['Masha','Sasha', 'Grisha']
students.append('Olga') #students= ['Masha','Sasha','Grisha','Olga']
students+='Olga' #students= ['Masha','Sasha','Grisha','Olga','Olga']
Пустой список students=[]

students.insert(1,'Dima') #students= ['Masha','Dima','Sasha','Grisha','Olga','Olga']

students= ['Masha','Sasha', 'Grisha']
students.remove('Sasha') #students= ['Masha', 'Grisha']
del students[0] #students= ['Grisha']

#сортировка списка
students= ['Masha','Sasha', 'Grisha']
ordered_students=sorted(students) #['Grisha','Masha','Sasha']
students.sort() #изменит саму переменную

min() #минимальное значение в списке
max() #максимальное значение в списке

чтобы применять функции к спискам, они должны быть сравнимы

#список в обратном порядке
students= ['Masha','Sasha', 'Grisha']
students.reverse() #students= ['Grisha','Sasha', 'Masha'] метод у списка, который изменяет сам список
reversed(students) #позволяет сделать тоже самое, но не изменять переменную
student[::-1] #изначальный список не изменится, будет копия списка, которая записана в противоположном порядке

#поиск элемента в списке
students= ['Masha','Sasha', 'Grisha']
if 'Sasha' in students:
         print('Sasha is here!') 
if 'Ann' not in students:
         print('Ann is out')

ind=index.students('Sasha') #ind=1

#генерация списков
a=[0]*5 #[0,0,0,0,0]
a=[0 for i in range(5)] #[0,0,0,0,0] list comprehension
a=[i*i for i in range(5)] #[0,1,4,9,16]
a=[int(i) for i in input().split()] 

#двумерные списки
a=[[1,2,3],[4,5,6],[7,8,9]]
a[1] #[1,2,3]
a[1][1] #5

#генерация двумерных списков
a=[[0]*n for i in range(n)]
a=[[0 for j in range(n)] for i in range(n)]


