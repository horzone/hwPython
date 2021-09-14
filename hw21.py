# -*- coding: utf-8 -*-


# Написать функцию-генератор, которая объединяет два отсортированных итератора.
# Результирующий итератор должен содержать последовательность в которой содержаться все элементы из каждой коллекции, в упорядоченном виде.
#  list(merge((x for x in range(1,4)),(x for x in range(2,5)))) == [1,2,2,3,3,4]


def merge(list1, list2):
    check_first_val = True
    check_second_val = True
    try:
        first_value = next(list1)
    except(StopIteration):
        check_first_val = False
        first_value = 0
    try:
        second_value = next(list2)
    except(StopIteration):
        second_value = 0
        check_second_val = False
    while True:
        if check_first_val and first_value <= second_value:
            try:
                yield first_value
                first_value = next(list1)
                continue
            except(StopIteration):
                check_first_val = False
                continue
        elif check_second_val and first_value >= second_value:
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


result = list(merge((x for x in range(-5, 10)), (x for x in range(1, 1))))

print(result)
