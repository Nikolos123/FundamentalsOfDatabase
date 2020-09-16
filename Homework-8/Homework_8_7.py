# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав
# экземпляры класса (комплексные числа) и выполнив сложение и
# умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, p1):
        self.p1 = p1

    def __add__(self, other):
        return self.p1 + other.p1

    def __gt__(self, other):
        return self.p1 > other.p1

    def __lt__(self, other):
        return self.p1 < other.p1

    def __ge__(self, other):
        return self.p1 >= other.p1

    def __le__(self, other):
        return self.p1 <= other.p1

    def __eq__(self, other):
        return self.p1 == other.p1


a = ComplexNumber(10)
b = ComplexNumber(20)

print(f"{a + b}")
print(f"{a > b}")
print(f"{a < b}")
print(f"{a <= b}")
print(f"{a >= b}")
print(f"{a == b}")



