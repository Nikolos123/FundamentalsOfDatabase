# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:
    is_police = bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f'Текущая скорость авто {self.speed}')

    def go(self):
        print(f'Поехала машина {self.name} '
              f'это полиция? {"нет" if self.is_police == False else "да"} '
              f'какой у нее цвет? {self.color}')

    def stop(self):
        print(f'Остановила машина {self.name}')


class TownCar(Car):
    speedt = 0
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.color = "Белый"
        self.name = "Lada kalina"
        self.is_police = False
        self.speed = speed

    def show_speed(self):
        if self.speed > 60:
            print(f'Текущая скорость привысила 60 км текущая скорость {self.speed} остановитесь')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.color = "Желтый"
        self.name = "Porsche 911"
        self.speed = 300
        self.is_police = False


class WorkClass(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.color = "Красный"
        self.name = "Копейка"
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print(f'Текущая скорость привысила 40 км  ваша скорость {self.speed} остановитесь')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.color = "Черный"
        self.name = "Chrysler"
        self.speed = 500
        self.is_police = True


t = WorkClass(42, '', '', '')
t1 = TownCar(62, '', '', '')
t2 = SportCar('', '', '', '')
t3 = PoliceCar('', '', '', '')
t1.go()
t1.show_speed()
t1.stop()
t2.go()
t2.show_speed()
t3.go()
t3.show_speed()
t.go()
t.show_speed()
t.stop()


# так как болел присылаю такой вариант. Можно было гонки устроить конечно
