# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class Myerror(Exception):
    def __init__(self, err):
        self.err = err


class MyException:
    @staticmethod
    def func_exception(a, b=100):
        try:
            if a == 0:
                raise Myerror("Деление на 0 невозможно")
            elif a > 0:
                print(round(b / a))
        except Myerror as err:
            print(err)


a = int(input('Введите число для деления на 100 '))
MyException.func_exception(a)
