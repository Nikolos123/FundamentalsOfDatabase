# ------------------------------------------

# Program by Nikolay.N.N
#
#
# Version       Date        Info
# 1.0           2020        Initial Version
#
# Student       GeekBrains  Fac:Python

# ------------------------------------------

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

a = int(input('Введите количество секунд для конвертации '))
if a > 1:
    print(f'Введенном числе  часов {int(a / 60 / 60)} минут {int(a / 60) - (int(a / 60 / 60) * 60)} сенкуд {a - (int(a / 60) * 60)}')
elif a == 0:
    print('Деленеи на 0 запрещено')
else:
    print('Вы ввели не верные данные')
