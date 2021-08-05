# -*- coding: utf-8 -*-


# The decimal number, 585 = 1001001001 in binary, is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2. (Please note that the palindromic number,
# in either base, may not include leading zeros.)
#
# Напишите программу, которая решает описанную выше задачу и печатает ответ.


# Функция проверяет, явлется ли заданное число палиндромом в десятичной и в 2ичной системе исчисления и
# возвращает True или False в зависимости от результата

def isPalindromic(checked_number):
    if str(checked_number) == str(checked_number)[::-1]:
        checked_number = bin(checked_number)[2:]
        if checked_number == checked_number[::-1]:
            return True
    else:
        return False


result = 0
for number in range(0, 1000000):
    if isPalindromic(number):
        result += number

print(result)
