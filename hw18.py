# -*- coding: utf-8 -*-
import os.path

from PIL import Image


# Написать скрипт, который будет создавать миниатюры фотографий.
# Объем полученого файла должен передаваться как параметр.


def compress(path, percent_of_compression):
    if percent_of_compression >= 100:
        print('cant compress more then 99%')
        exit()
    elif percent_of_compression <= 0:
        print('cant compress less then 1%')
        exit()
    image = Image.open(path)
    w, h = image.size
    w = int(w * (100 - percent_of_compression) / 100)
    h = int(h * (100 - percent_of_compression) / 100)
    new_size = (w, h)
    new_image = image.resize(new_size)
    path = path.split(sep='.')
    path[0] = path[0] + f'_{percent_of_compression}%'
    new_path = '.'.join(path)
    new_image.save(new_path)


if __name__ == '__main__':
    compress('IMG_8535.JPG', 10)
    compress('IMG_8535.JPG', 30)
    compress('IMG_8535.JPG', 60)
    compress('IMG_8535.JPG', 90)
