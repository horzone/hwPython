# -*- coding: utf-8 -*-
import copy
# Надо написать функцию которая возвращает N-мерный массив с ширинами заданными в аргументе списком из N элементов:
# n_arr([2,2])
# >> [[“”,“”],[“”,“”]]
# n_arr([2,2,2])
# >> [[[“”,“”],[“”,“”]], [[“”,“”],[“”,“”]]]


def n_arr(size):
    element = ('!')
    no_result = []
    for _ in range(0, size[0]):
        no_result.append(element)
    next_count = copy.deepcopy(no_result)
    for i in range(1, len(size)):
        prev_count = [copy.deepcopy(next_count)]
        for j in range(0, size[i] - 1):
            prev_count.append(copy.deepcopy(next_count))
            if size[i] - (j + 2) == 0:
                next_count = copy.deepcopy(prev_count)
    return next_count


a = n_arr([1, 3, 3])
print(a)
