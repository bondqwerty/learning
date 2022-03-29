Недавно мы считали для каждого слова количество его вхождений в строку. 
Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.

Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то,
сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).

В качестве ответа укажите вывод программы, а не саму программу.

Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input:
abc a bCd bC AbC BC BCD bcd ABC

Sample Output:
abc 3

with open("dataset_3363_3.txt", "r") as f:
    str0= f.read() 

def count_words(str0):
    str0 = str0.lower()
    count = {}
    dict_max={}
    words = str0.split()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    #for i in count:
        #print (i, count[i])
    maxim = max(count, key=count.get)  
    tup=(maxim, count[maxim])
    str1 = ' '
    str1=str1.join([str(value) for value in tup])
    return str1
    
count_words(str0)

ouf=open('easy.txt','w')
ouf.write(count_words(str0))           
ouf.close()
