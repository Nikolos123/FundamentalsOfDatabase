# ------------------------------------------

# Program by Nikolay.N.N
#
#
# Version       Date        Info
# 1.0           2020        Initial Version
#
# Student       GeekBrains  Fac:Python

# ------------------------------------------

# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().


a = int(input('Введите число'))

list1 = [i for i in range(a)]
b = len(list1)
print(list1)
if b % 2 == 0:
    for key, value in enumerate(list1):
        if key % 2 == 0:
            list1[key] = value + 1
            list1[key + 1] = value
            print(key, value)
else:
    for key, value in enumerate(list1[:-1]):
        if key % 2 == 0:
            list1[key] = value + 1
            list1[key + 1] = value
            print(key, value)
print(list1)
