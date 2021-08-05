# -*- coding: utf-8 -*-
import pickle


# Создать сотрудника Mary, пользуясь классом
# Employee и перенести его в другую программу,
# используя модуль Pickle и файловую систему.
# Узнать про + и - модуля Pickle.

# Можно спрятать в битовой последовательности любую функцию, и при импорте она сработает (возможна вреданосная)

# 1) создали Класс Employee, переопределили метод __init__.
# 2) создали экземпляр класса и записали его в mary.
# 3)
# 4) записали с помощью pickle mary в фаил
#
#
# Главные минус pickle, что он не безопасный
# с помощью него можно загрузить и не зная этого запустить все что угодно,
# в том числе и вредоносный код
#
#
#
# 5) открыли фаил HW14export в режиме побайтового чтения
# 6) с помощью pickle преобразовали поток байтов из файла в объект Python, а иммено в экземпляр
# класса Employee и записали в новую переменную new_mary


class Employee:
    def __init__(self, name):
        self.name = name


mary = Employee('Mary')

with open('HW14export', 'wb') as export_file:
    pickle.dump(mary, export_file)

with open('HW14export', 'rb') as import_file:
    new_mary = pickle.load(import_file)


print(new_mary.name)
