# -*- coding: utf-8 -*-

# 1. После запуска предлагает пользователю ввести неотрицательные целые числа,
# разделенные через пробел и ожидает ввода от пользователя.
# 2. Находит наименьшее положительное число, не входящее в данный пользователем
# список чисел и печатает его.

def function(my_input):
    result = []
    for i in range(0, len(my_input)):
        if my_input[i].isdigit():
            result.append(int(my_input[i]))
    for i in range(1, max(result)+1):
        if i not in result:
            print(i)
            return
        elif i == (max(result)):
            print(i+1)


print("Введите неотрицательные целые числа, разделенные через пробел: ")
function(input())
