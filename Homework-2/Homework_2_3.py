# ------------------------------------------

# Program by Nikolay.N.N
#
#
# Version       Date        Info
# 1.0           2020        Initial Version
#
# Student       GeekBrains  Fac:Python

# ------------------------------------------

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
c = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
p = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август', 9: 'Сентябрь',
     10: 'Октябрь',
     11: 'Ноябрь', 12: 'Декабрь'}
a = int(input('Введите число от 1 - 12'))
d = 0
for i, v in c.items():
    for t in v:
        if t == a:
            print(f'Время года {i}, а месяц {p[t]}')
