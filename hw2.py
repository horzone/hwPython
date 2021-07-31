# -*- coding: utf-8 -*-


def function(my_input):
    my_input = set(my_input.split(sep=" "))
    print(" ".join(my_input))


print("Введите Ваш текст: ")
function(input())
