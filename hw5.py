# -*- coding: utf-8 -*-


def function(my_input):
    my_input = my_input.split(sep=" ")
    my_input = [int(i) for i in my_input]
    result = 1
    for i in set(my_input):
        if result in my_input:
            result += 1
        else:
            print(result)
            exit()


print("Введите неотрицательные целые числа, разделенные через пробел: ")
function(input())
