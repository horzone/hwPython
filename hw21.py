# -*- coding: utf-8 -*-


# Написать функцию-генератор, которая объединяет два отсортированных итератора.
# Результирующий итератор должен содержать последовательность в которой содержаться все элементы из каждой коллекции, в упорядоченном виде.
#  list(merge((x for x in range(1,4)),(x for x in range(2,5)))) == [1,2,2,3,3,4]


def merge(list1, list2):
    list1 = list(list1)
    list2 = list(list2)
    for i in list(zip(list1, list2)):
        for j in range(0, 2):
            yield i[j]


result = list(merge((x for x in range(1, 4)), (x for x in range(2, 5))))

print(result)
