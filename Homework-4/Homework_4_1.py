# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия.
# # Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


def salary(script_name, v_hour, s_hour, prize=argv):
    print("name: ", script_name)
    print("my salary: ", v_hour*s_hour+prize)
    # print("param 2: ", s_hour)
    # print("param 3: ", prize)


# #
# # #Вызов знаю что вы сказали что вызов не нужен но все же
# # #python -c "import Homework_4_1; Homework_4_1.salary('Nikolay',10,5,100)"

