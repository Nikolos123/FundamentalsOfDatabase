# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
import os

a = "1"
file_name = "task1.txt"

try:
    os.remove(file_name)
except FileNotFoundError:
    print("файла нет")
else:
    print("Старый файл удален")


while a != "":
    a = input('Введите слова и оно будет записано в файл')
    if a != "":
        with open(file_name, "a+", encoding="utf-8") as f:
            print(a, file=f)
