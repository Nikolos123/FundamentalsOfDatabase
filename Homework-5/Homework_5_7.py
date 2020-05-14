# 7. Создать (не программно) текстовый файл, в котором каждая
# строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль
# каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import pytils.translit
import re
import json

dict1 = {}
dict2 = {}
list1 = []
with open("text_7.txt", 'r', encoding='utf-8') as f:
    ff = ['1']
    p = {}
    isum = 0
    icol = 0
    while len(ff) >= 0:
        c = f.readline()
        ff = re.findall(r'\d+', c)
        dd = (re.findall(r'\w+\D+', c))
        if len(ff) == 0:
            break
        summa = int(ff[0]) - int(ff[1])

        if summa > 0:
            dict1.update({pytils.translit.translify(dd[0][:-1]): summa})
            isum += summa
            icol += 1
        else:
            dict1.update({pytils.translit.translify(dd[0][:-1]): summa})
    dict2 = {"average_profit": isum / icol}
    list1.append(dict1)
    list1.append(dict2)
print(list1, '\n')
print('*' * 100 + 'JSON')
print(dict1)
print(dict2)
with open("m.json", "w")as my_j:
    json.dump(list1, my_j, sort_keys=True, indent=5)
