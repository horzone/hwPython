# -*- coding: utf-8 -*-

from GPSPhoto import gpsphoto
from hw16 import function as hw16_function
# Написать скрипт, который будет вытаскивать gps данные
# из фотографии (jpg файл) и передавать их на вход программе
# из hw16.txt

data = gpsphoto.getGPSData('IMG_8535.JPG')
latlng = f"{data['Latitude']} , {data['Longitude']}"

hw16_function(latlng)