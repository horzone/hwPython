# -*- coding: utf-8 -*-
from functools import reduce

# problem9 - list comprehension : one line
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


# hw9 - 9 долго считает. Я не дождался.


result = [b * a * ((1000 - a) - b) for b in range(1, 1001) for a in range(1, b) if
          a ** 2 + b ** 2 == ((1000 - a) - b) ** 2]

print(result)
