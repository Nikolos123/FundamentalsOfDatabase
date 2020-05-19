# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color
# (цвет) и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния
# (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
# на ваше усмотрение. Переключение между режимами должно осуществляться только
# в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.
import time
import asyncio


class TrafficLight:
    # атрибуты
    def __init__(self, color):
        self.__color = color

    def star_color(self):
        print(f"сейчас горит {self.__color}")


async def timeout(colo_r, sleep_color):
    traf = TrafficLight(colo_r)
    traf.star_color()
    time.sleep(sleep_color)


async def output(sleep):
    while sleep > 0:
        await asyncio.sleep(1)
        print(f'{sleep} seconds')
        sleep -= 1


async def main():
    i = 1
    while True:
        if i == 1:
            task_1 = asyncio.create_task(timeout('Красный', 0))
            task_2 = asyncio.create_task(output(7))
            await task_1
            await task_2
        elif i == 2:
            task_1 = asyncio.create_task(timeout('Желтый', 0))
            task_2 = asyncio.create_task(output(2))
            await task_1
            await task_2
        elif i == 3:
            task_1 = asyncio.create_task(timeout('Зелёный', 0))
            task_2 = asyncio.create_task(output(5))
            await task_1
            await task_2
        if i == 3:
            i = 1
        else:
            i += 1


asyncio.run(main())

# надеюсь мое усложнение засчитается вместо того что нужно было. Так проверка порядка тут не нужна
