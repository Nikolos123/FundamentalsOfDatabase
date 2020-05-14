# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4

import string

dic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', }
t = string.ascii_letters

c = ''
with open("text_4.txt", 'r', encoding='utf-8') as f:
    with open("text_41.txt", 'w', encoding='utf-8') as d:
        for i in f:
            iii = ''
            ttt = ''
            for ii in i:
                if ii in t:
                    iii += ii
                else:
                    ttt += ii
            print(dic[iii] + ttt, end='', file=d)
