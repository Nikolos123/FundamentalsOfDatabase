# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
#


def my_funck(name, fam, year, city, email, tel):
    print(
        f'Меня зовут {name} и фамилия моя {fam} год рождения {year} город проживания {city} email {email} телефон {tel}')


a = input('Введите ваше имя ')
b = input('Введите вашу фамилию ')
c = input('Введите год рождения ')
d = input('Введите город ')
i = input('Введите email ')
f = input('Введите телефон ')

my_funck(fam=b, tel=f, name=a, city=d, year=c, email=i)
