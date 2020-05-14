# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random
import os

os.remove("test2.txt")
with open('test2.txt', 'w', encoding="utf-8") as f:
    a = (random.randint(1000, 50000) for _ in range(2))
    for i in a:
        print(i)
        f.write(str(i) + " ")

with open("test2.txt", "r", encoding="utf-8") as s:
    print('*' * 50)
    z = 0
    for i in s:
        for ii in i.split(' '):
            if ii != '':
                z = z + int(ii)
    print(f'Сумма {z}')
