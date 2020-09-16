# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу
# «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
import calendar


class Myerror(Exception):
    def __init__(self, err):
        self.err = err


class Date:
    @classmethod
    def one(self, a):
        self.a = a

        c = {0: 'День', 1: 'Месяц', 2: 'Год'}
        b = [i for i in a.split('-')]
        for i in b:
            print(f'{c[int(b.index(i))]} {int(i)}')
        # Этот варинат лучше так как можно нарваться на дату 12-12-2012 и тогда нужно будет еще обработать
        # print(f'День{int(b[0])}')
        # print(f'Месяц{int(b[1])}')
        # print(f'Год{int(b[1])}')

    @staticmethod
    def two(a):
        b = [i for i in a.split('-')]
        try:
            i = calendar.monthrange(int(b[2]), int(b[1]))[1]
            if i < int(b[0]):
                raise Myerror("Такого дня в месяце не существует")
        except calendar.IllegalMonthError:
            print('Не верно ввели месяц введити от 1-12')
        except Myerror as err:
            print(err)


a = input('Введите дату в формате 12-01-2012 ')
met = Date()
met.one(a)
Date.two(a)
