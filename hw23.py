# -*- coding: utf-8 -*-
# Надо написать функцию которая возвращает N-мерный массив с ширинами заданными в аргументе списком из N элементов:
# n_arr([2,2])
# >> [[“”,“”],[“”,“”]]
# n_arr([2,2,2])
# >> [[[“”,“”],[“”,“”]], [[“”,“”],[“”,“”]]]


def n_arr(size):
    element = "!"
    no_result = []
    for _ in range(0, size[0]):
        no_result.append(element)
    next_count = list(no_result)
    for i in range(1, len(size)):
        prev_count = list([next_count])
        for j in range(0,size[i]-1):
            prev_count.append(list(next_count))
            if size[i] - (j+2) == 0:
                next_count = list(prev_count)
    print(next_count)


n_arr([2, 2])
n_arr([2, 2, 2])
n_arr([2, 2, 2, 2])
n_arr([2, 2, 2, 2, 2])
n_arr([2, 2, 2, 2, 2, 2])