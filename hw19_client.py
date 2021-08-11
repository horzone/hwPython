# -*- coding: utf-8 -*-
# ADD ya.ru:8.8.8.8
import socket
# Создаем сокет
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Просим ввессти запрос
message = input("Input domain name: ")
# Если запрос на выключение DNS сервера, то освобождаем сокет и выходим из выполнения скрипта
if message == "shutdown":
    client.close()
    exit()
# Отправляем наш запрос на сервер
client.sendto(bytes(message, 'utf-8'), ('127.0.0.1', 4041))
# Получаем ответ от сервера
data, address = client.recvfrom(4041)
# Освобождаем сокет
client.close()
# Выводим результат
print(data.decode())
