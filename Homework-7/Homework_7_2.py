# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда,
# которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


from abc import ABC, abstractmethod

from abc import ABC, abstractmethod


class MyAbCl(ABC):
    @abstractmethod
    def get_kost(self):
        return f'Расход для костюма {str(self.VH)}'

    @abstractmethod
    def get_palt(self):
        return f'Расход на пальто {str(self.VH)}'


class MyClass(MyAbCl):
    def __init__(self, VH, HV):
        if HV == 0:
            self.VH = 2 * VH + 0.3
        elif VH == 0:
            self.VH = HV / 6.5 + 0.5
        else:
            self.VH = 0

    @property
    def VH(self):
        return self.__VH

    @VH.setter
    def VH(self, VH):
        self.__VH = VH

    def get_kost(self):
        return f'Расход на костюма {str(self.VH)}'

    def get_palt(self):
        return f'Расход на пальто {str(self.VH)}'


my_1 = MyClass(10, 0)
print(my_1.get_kost())

my_1 = MyClass(0, 10)
print(my_1.get_palt())
