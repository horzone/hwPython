# -*- coding: utf-8 -*-

# Написать функцию Фиббоначи fib(n), которая вычисляет
# элементы последовательности Фиббоначи:
# 1 1 2 3 5 8 13 21 34 55 .......

def fib(n):
    result = []
    a, b = 1, 1
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result[n-1]


print(fib(5432))