# -*- coding: utf-8 -*-
# ADD ya.ru:8.8.8.8
import socket
# Создаем сокет
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    # Просим ввессти запрос
    message = input("Input domain name(*shutdown* for exit and shutdown server): ")
    # Отправляем наш запрос на сервер
    client.sendto(bytes(message, 'utf-8'), ('127.0.0.1', 4041))
    # Если запрос на выключение DNS сервера, то выходим из цикла
    if message == "shutdown":
        break
    # Получаем ответ от сервера
    data, address = client.recvfrom(4041)
    # Выводим результат
    print(data.decode())
# Освобождаем сокет
client.close()
