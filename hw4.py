# -*- coding: utf-8 -*-


def function(my_input):
    result = []
    for i in my_input:
        if i.isnumeric():
            result.append(i)
        else:
            result.append(" ")
    result = "".join(result)
    result = result.split(sep=" ")
    test = 0
    for j in result:
        if j.isnumeric():
            test += int(j)
    print(test)


print("Введите Ваш текст: ")
function(input())
