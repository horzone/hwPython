# -*- coding: utf-8 -*-

def isPalendromic(checked_number):
    if str(checked_number) == str(checked_number)[::-1]:
        checked_number = bin(checked_number)[2:]
        if checked_number == checked_number[::-1]:
            return True
    else:
        return False


result = 0
for number in range(0, 1000000):
    if isPalendromic(number):
        result += number

print(result)
