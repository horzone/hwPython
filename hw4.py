# -*- coding: utf-8 -*-


def function(my_input):
    input_line = []
    for i in range(0, len(my_input)):
        if my_input[i].isnumeric():
            input_line.append(my_input[i])
        elif my_input[i] == "-" and my_input[i+1].isnumeric():
            input_line.append(my_input[i])
        else:
            input_line.append(" ")
    input_line = "".join(input_line)
    input_line = input_line.split(sep=" ")
    result = 0
    for j in input_line:
        if j != "":
            result += int(j)
    print(result)


print("Введите Ваш текст: ")
function(input())
