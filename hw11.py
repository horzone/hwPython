# -*- coding: utf-8 -*-


# Напишите функцию letters_range, которая ведет себя
# похожим на range образом, однако в качестве start и
# stop принимает не числа, а буквы латинского алфавита
# (в качестве step принимает целое число) и возращает
# не перечисление чисел, а список букв, начиная с
# указанной в качестве start, до указанной в качестве
# stop с шагом step (по умолчанию равным 1).
#
# Пример:
# >>>letters_range('b', 'w', 2)
# ['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v']
#
# >>>letters_range('a', 'g')
# ['a', 'b', 'c', 'd', 'e', 'f']
#
# >>>letters_range('g', 'p')
# ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
#
# >>>letters_range('p', 'g', -2)
# ['p', 'n', 'l', 'j', 'h']
#
# >>>letters_range('a','a')
# []

def letters_range(start, stop, step=int(1)):
    letters_chars = [chr(char) for char in range(97, 123)]
    index_start = letters_chars.index(start)
    index_stop = letters_chars.index(stop)
    result = [letters_chars[i] for i in range(index_start, index_stop, step)]
    print(result)


letters_range('a', 'g')
