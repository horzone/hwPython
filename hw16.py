# -*- coding: utf-8 -*-
from geopy.geocoders import Nominatim

# Написать программу, которая будет считывать из файла gps координаты,
# и формировать текстовое описание объекта и ссылку на google maps.
# Пример:
#
# Input data: 60,01';30,19'
# Output data:
# Location: Теремок, Енотаевская улица, Удельная, округ Светлановское, Выборгский район, Санкт-Петербург, Северо-Западный федеральный округ, 194017, РФ
# Goggle Maps URL: https://www.google.com/maps/search/?api=1&query=60.016666666666666,30.322

def function(latlng):
    geo = Nominatim(user_agent="my_app")
    request = geo.reverse(latlng)
    print(f'Location: {request.address}')
    print(f'Google Maps URL: https://www.google.com/maps/search/?api=1&query={latlng}')

if __name__ == '__main__':
    with open('gps.txt', 'r') as my_file:
        for line in my_file:
            function(latlng=line)
