Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.

На вход программе первой строкой передаётся количество dd известных нам слов, после чего на dd строках указываются эти слова. Затем передаётся количество ll строк текста для проверки, после чего ll строк текста.

Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

Sample Input:
4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic

Sample Output:
stepic
champignons
the





d = int(input())
list1 = []

for i in range(d):
    s = str(input())
    s = s.lower()
    list1 = list1 + s.split(' ')

list2 = []
l = int(input())
for j in range(l):
    d = str(input())
    d = d.lower()
    list2 = list2 + d.split(' ')
 
main_list = list(set(list2) - set(list1))
for i in range(len(main_list)):
    print(main_list[i])
