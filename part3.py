#Функции
def min2(a,b): #def имя функции (аргументы(параметры))
  if a <= b: #тело функции
    return a
  else:
    return b
  
m = min2(42,35)
m = min2(min2(42,35),6)
  
  
#Произвольное число параметров
def min(*a):
  m = a[0]
  for x in a:
    if m > x:
      m = x
    return m 
  
#Значение параметров по умолчанию
def my_range(start, stop, step=1):
    res = []
    if step > 0:
        x = start
        while x < stop:
            res += [x]
            x += step
    elif step < 0:
        x = start
        while x > stop:
            res += [x]
            x += step
    return res
  
#Локальные переменные
def init_values():
    a = 100
    b = 200
    
init_values()
print(a + b)  # Ошибка, переменные a и b не объявлены

#Глобальные переменные - переменные, которые объявлены вне функции

#Множества
s=set() #создание пустого множества

basket = {'orange','apple','apple','pear','apple'}
print(basket) #orange, banana, pear, apple
'orange' in basket #True
'python' in basket #False


#Операции с множествами
basket.add(element)
basket.remove(element)
basket.discard(element)
basket.clear()


#Словари
dict, {} #пустой словарь
d = {'a': 234, 10: 100}
print(d['a'])
print(d[10])

#Операции со словарями
dictionary = {...}
key in dictionary 
key not in dictionary
dictionary[key]=value
dictionary[key]
dictionary.get(key)
del dictionary[key]


#Модули
from my_module import foo() #импортируем конкретную функцию
from my_module import * #импортируем все
from my_module import foo() as my_foo() #импортируем конкретную функцию и переназываем ее



