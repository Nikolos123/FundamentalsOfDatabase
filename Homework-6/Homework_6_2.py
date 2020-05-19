# 2. Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна. Использовать
# формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги
# асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def __init__(self, length, width, sm=5, kg=25):
        self._length = length
        self._width = width
        self._sm = sm
        self._kg = kg

    def Road_length_width(self):
        a = self._length * self._width * self._kg * self._sm
        a = str(a)
        print(f"Масса асфальта =  {a[:5]} т")


startRoad = Road(20, 5000)
startRoad.Road_length_width()
