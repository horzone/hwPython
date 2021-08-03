# -*- coding: utf-8 -*-
import pickle


# Создать сотрудника Mary, пользуясь классом
# Employee и перенести его в другую программу,
# используя модуль Pickle и файловую систему.
# Узнать про + и - модуля Pickle.

# Можно спрятать в битовой последовательности любую функцию, и при импорте она сработает (возможна вреданосная)






class Employee:
    def __init__(self, name):
        self.name = name


mary = Employee('Mary')

with open('HW14export', 'wb') as export_file:
    pickle.dump(mary, export_file)

