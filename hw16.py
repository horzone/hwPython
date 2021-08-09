# -*- coding: utf-8 -*-
import googlemaps


# Написать программу, которая будет считывать из файла gps координаты,
# и формировать текстовое описание объекта и ссылку на google maps.
# Пример:
#
# Input data: 60,01';30,19'
# Output data:
# Location: Теремок, Енотаевская улица, Удельная, округ Светлановское, Выборгский район, Санкт-Петербург, Северо-Западный федеральный округ, 194017, РФ
# Goggle Maps URL: https://www.google.com/maps/search/?api=1&query=60.016666666666666,30.322

def function(latlng):
    me = googlemaps.Client(key='AIzaSyCrEsxkaBbNDuk5agv0boIj6QttGxv7tRs')
    request = googlemaps.client.reverse_geocode(latlng=latlng, client=me, language='ru')
    place_id = request[0]['place_id']
    place_address = request[0]['formatted_address']
    place_request = googlemaps.client.place(place_id=place_id, fields=["name", "url"], language='ru',
                                            client=me)
    place_name = place_request['result']['name']
    place_url = place_request['result']['url']
    print(f'Location: {place_name}, {place_address}')
    print(f'Google Maps URL: {place_url}')


if __name__ == 'main':
    with open('gps.txt', 'r') as my_file:
        for line in my_file:
            function(latlng=line)
