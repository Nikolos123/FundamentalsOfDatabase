# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    t = sorted([a, b, c])
    print(t[2] + t[1])


my_func(77, 3, 65)
