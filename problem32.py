Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.


import requests

link = 'https://stepic.org/media/attachments/course67/3.6.3/'

with open('seq.txt') as in_f_obj:
	url = in_f_obj.read().strip()

r = requests.get(url)
r = link + r.text

flag = True

while flag == True:
    r = requests.get(r)
    
    if (r.text.count('.txt')):
        r = link + r.text

    else:
        flag = False
        fin = r.text

with open('easy.txt', 'w') as out_f_obj:
	out_f_obj.write(str(fin))

