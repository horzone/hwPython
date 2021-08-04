# -*- coding: utf-8 -*-
# 1. После запуска предлагает пользователю ввести целые неотрицательные числа,
# разделенные любым не цифровым литералом (пробел, запятая, %, буква и т.д.).
# 2. Получив вводные данные, выделяет полученные числа, суммирует их,
# и печатает полученную сумму.

def function(my_input):
    input_line = []
    for i in range(0, len(my_input)):
        if my_input[i].isnumeric():
            input_line.append(my_input[i])
        elif my_input[i] == "-" and my_input[i+1].isnumeric():
            if my_input[i+1].isnumeric():
                input_line.append(" ")
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
function('324k32h43k2jh423kj4h2-351')
