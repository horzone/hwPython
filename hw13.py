# -*- coding: utf-8 -*-


# Напишите функцию, которая переводит значения показаний температуры из Цельсия в Фаренгейт и наоборот.

# hw13 - зачем lower() ?
# что бы работало любое указание размерности (F и f, C и c) в не зависимости от регистра
def change_temp(temp, dimension):
    if dimension.lower() == 'c':
        result = temp * 1.8 + 32
    elif dimension.lower() == 'f':
        result = (temp - 32) * (5 / 9)
    else:
        return 'incorrect dimension (need F or C)'
    return round(result, 2)


print(change_temp(1, 'f'))
