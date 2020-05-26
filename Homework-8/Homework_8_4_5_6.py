# 4. Начните работу над проектом «Склад оргтехники». Создайте
# класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
#
# 5. Продолжить работу над первым заданием. Разработать методы,
# отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
#
# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте
# «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class Myerror(Exception):
    def __init__(self, err):
        self.err = err


class Sklad:
    @staticmethod
    def my_func(skald, departamens, kol):
        a = {"sklad": '', "departamens": '', 'kol': 0}
        try:
            if type(kol) != int:
                raise Myerror("Параметр количество не является числом")
            else:
                a["sklad"] = skald
                a["departamens"] = departamens
                a["kol"] = kol
                print(a)
        except Myerror as err:
            print(err)


class OrgTeh:
    def __init__(self, tip, sum, name, model):
        self.tip = tip
        self.sum = sum
        self.name = name
        self.model = model


class Print(OrgTeh, Sklad):
    def __init__(self, tip, sum, name, model, speedprint):
        super().__init__(tip, sum, name, model)
        self.speedprint = speedprint

    def characteristic(self):
        print(f'\033[31m Характеристика')

        print(f'\033[30mИмя принтера:{self.name} \nМодель принтера:{self.model} \nТип:{self.tip} \n'
              f'Скорость печати:{self.speedprint} \nСкорость печати:{self.speedprint}')

        print("*" * 50)


class Scan(OrgTeh, Sklad):
    def __init__(self, tip, sum, name, model, speedscan):
        super().__init__(tip, sum, name, model)
        self.speedscan = speedscan

    def characteristic(self):
        print(f'\033[31m Характеристика')

        print(f'\033[30mИмя принтера:{self.name} \nМодель принтера:{self.model} \nТип:{self.tip} \n'
              f'Скорость печати:{self.speedscan} \nСкорость печати:{self.speedscan}')

        print("*" * 50)


class Copy(OrgTeh, Sklad):
    def __init__(self, tip, sum, name, model, speedcopy):
        super().__init__(tip, sum, name, model)
        self.speedcopy = speedcopy

    def characteristic(self):
        print(f'\033[31m Характеристика')

        print(f'\033[30mИмя принтера:{self.name} \nМодель принтера:{self.model} \nТип:{self.tip} \n'
              f'Скорость печати:{self.speedcopy} \nСкорость печати:{self.speedcopy}')

        print("*" * 50)


my_1 = Print('Принтер', 5000, 'Kyosera', '1018', 1000)
my_1.characteristic()

my_1 = Copy('Крерокс', 500, 'Kyosera', '1528', 500)
my_1.characteristic()

my_1 = Scan('Сканер', 5000, 'Kyosera', '1789', 300)
my_1.characteristic()

my_1.my_func('opt', 'it', 100)
# my_1.my_func('opt', 'it', 'e') проверка ошибки
