# -*- coding: utf-8 -*-


# problem9 - list comprehension : one line
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for c in range(1, 1000):
    for b in range(1, c):
        for a in range(1, b):
            if a ** 2 + b ** 2 == c ** 2:
                if a + b + c == 1000:
                    print("{} {} {}".format(a, b, c))


