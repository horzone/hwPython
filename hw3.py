# -*- coding: utf-8 -*-

def function(my_input):
    my_input = my_input.split(sep=" ")
    result = {}
    for i in my_input:
        if i.lower() in result.keys():
            result[i.lower()] += 1
        else:
            result[i.lower()] = 1

    for name, quantity in result.items():
        if quantity == max(result.values()):
            print("{} - {}".format(quantity, name))


while True:
    print("Введите Ваш текст(для выхода наберите 0): ")
    my_input = input()
    if my_input == "0":
        exit()
    function(my_input)
