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


class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __add__(self, other):
        c = []
        for i in range(len(self.my_list)):
            c.append([])
            for j in range(len(self.my_list)):
                c[i].append(self.my_list[i][j] + other.my_list[i][j])
        return '\n'.join(map(str, c))

    def __str__(self):
        return '\n'.join(map(str, self.my_list))


matrix_1 = Matrix(matrix)
matrix_2 = Matrix(matrix)

print(f"Matrix 1\n{matrix_1}\n{'-' * 20}")
print(f"Matrix 2\n{matrix_2}\n{'-' * 20}")
print(f"{matrix_1 + matrix_2}\n{'-' * 20}")
