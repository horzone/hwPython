# -*- coding: utf-8 -*-


# The decimal number, 585 = 1001001001 in binary, is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2. (Please note that the palindromic number,
# in either base, may not include leading zeros.)
#
# Напишите программу, которая решает описанную выше задачу и печатает ответ.


# hw6: ПалИндром. Что возвращает функция?
# изменил фунцию

def isPalindromic_less_million():
    result = 0
    for checked_number in range(0, 1000000):
        if str(checked_number) == str(checked_number)[::-1]:
            checked_number_bin = bin(checked_number)[2:]
            if checked_number_bin == checked_number_bin[::-1]:
                result += int(checked_number)
    print(result)


isPalindromic_less_million()