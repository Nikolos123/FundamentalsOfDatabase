# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
# первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
import random

SIZE = 5
matrix = [[random.randint(1, 20) for _ in range(SIZE)] for _ in range(SIZE)]
matrix1 = [[random.randint(1, 20) for _ in range(SIZE)] for _ in range(SIZE)]
matrix2 = [[random.randint(0, 0) for _ in range(SIZE)] for _ in range(SIZE)]


class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __add__(self, other):
        return Matrix(self.my_list + other.my_list)

    def __str__(self):
        return f'{self.my_list}'


matrix_1 = Matrix(matrix)
matrix_2 = Matrix(matrix1)
result = matrix2
for i in range(len(matrix_1.my_list)):

    for j in range(len(matrix_1.my_list[0])):
        result[i][j] = matrix_1.my_list[i][j] + matrix_2.my_list[i][j]

for line in result:
    for item in line:
        print(f'{item:>4}', end='')
    print()

print('-' * (len(matrix)) * 4)
