# 6. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
#     Функция отвечает за получение факториала числа, а
#     в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
#     Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.четны

import math,random
def fac(n):
    for i in n:
        yield math.factorial(i)
a = [random.randint(1,10) for _ in range(20)]
print(a)
g = fac(a)
print(list(g))
