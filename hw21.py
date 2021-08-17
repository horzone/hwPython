# -*- coding: utf-8 -*-


# Написать функцию-генератор, которая объединяет два отсортированных итератора.
# Результирующий итератор должен содержать последовательность в которой содержаться все элементы из каждой коллекции, в упорядоченном виде.
#  list(merge((x for x in range(1,4)),(x for x in range(2,5)))) == [1,2,2,3,3,4]


def merge(list1, list2):
    first_value = next(list1)
    second_value = next(list2)
    check_first_val = True
    check_second_val = True
    while True:
        if first_value <= second_value and check_first_val:
            try:
                yield first_value
                first_value = next(list1)
                continue
            except(StopIteration):
                check_first_val = False
                continue
        elif first_value >= second_value and check_second_val:
            try:
                yield second_value
                second_value = next(list2)
                continue
            except(StopIteration):
                check_second_val = False
                continue
        else:
            try:
                if first_value > second_value:
                    yield first_value
                    first_value = next(list1)
                    continue
                if first_value < second_value:
                    yield second_value
                    second_value = next(list2)
                    continue
                if first_value == second_value:
                    break
            except(StopIteration):
                break


result = list(merge((x for x in range(1, 4)), (x for x in range(2, 5))))

print(result)
