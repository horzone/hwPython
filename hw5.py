# -*- coding: utf-8 -*-

# 1. После запуска предлагает пользователю ввести неотрицательные целые числа,
# разделенные через пробел и ожидает ввода от пользователя.
# 2. Находит наименьшее положительное число, не входящее в данный пользователем
# список чисел и печатает его.

def function(my_input):
    my_input = my_input.split(sep=" ")
    my_input = [int(i) for i in my_input]
    for i in range(1, max(my_input)+1):
        if i not in my_input:
            print(i)
            return
        elif i == (max(my_input)):
            print(i+1)


print("Введите неотрицательные целые числа, разделенные через пробел: ")
function(input())
