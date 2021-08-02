# -*- coding: utf-8 -*-

# problem40 - list comprehension
#
# An irrational decimal fraction is created by concatenating the positive integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value of the following expression.
#
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

digit = "".join([str(x) for x in range(1, 1000000)])
degree = [(10 ** x) - 1 for x in range(0, 7)]
result = 0
for i in degree:
    result += (int(digit[i]))

print(result)