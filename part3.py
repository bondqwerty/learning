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

  
