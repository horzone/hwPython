# -*- coding: utf-8 -*-


def function(my_input):
    input_line = []
    for i in my_input:
        if i.isnumeric():
            input_line.append(i)
        else:
            input_line.append(" ")
    input_line = "".join(input_line)
    input_line = input_line.split(sep=" ")
    result = 0
    for j in input_line:
        if j.isnumeric():
            result += int(j)
    print(result)


print("Введите Ваш текст: ")
function(input())
