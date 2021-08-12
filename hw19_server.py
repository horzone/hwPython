# -*- coding: utf-8 -*-
import socket

# Написать dns сервер.
# Сервер должен принимать соединения по протоколу udp.
# Если приходит запрос "domain.name" должен отправлять в ответ ip адрес.
# * Доп задание: иметь возможность переопределять записи клиентами:
# * ADD my.google.com:228.228.228.228


# Создаем сокет и закрепляем ему 127.0.0.1:4041
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 4041))
# В этой переменной будет хранится переопределенные нами записи
dns_cache = {}
# Запускаем цикл обработки
while True:
    # Получаем данные и адресс отправителя (4048 - размер буфера)
    data, address = server.recvfrom(4048)
    # Проверям, хотят ли выключить DNS сервер
    if data.decode() == "shutdown":
        # Освобождаем сокет
        server.close()
        # завершаем выполнение скрипта
        exit()
    # Проверяем первые 3 символа, если они ADD то переходим к переопредилению записей
    if data.decode()[0] == 'A' and data.decode()[1] == 'D' and data.decode()[2] == 'D':
        # Убираем лишнее из строки
        string_data_to_add = data.decode()[4:]
        # Разделяем строку делиметром ":"
        data_to_add = string_data_to_add.split(sep=':')
        # Заносим запись в словарь
        dns_cache[data_to_add[0]] = data_to_add[1]
        # Отправляем сообщение о том, что запись добавлена
        server.sendto(bytes('new record added', 'utf-8'), address)
        # Запускаем цикл заново
        continue
    # Если запрашиваемая запись переопределена на сервере, возвращаем переопределенную
    if data.decode() in dns_cache:
        name = dns_cache[data.decode()]
    else:
        # Если запись не переопределена, определяем hostname и возвращаем его
        name = socket.gethostbyname(f'{data.decode()}')
    # Отправляем информацию клиенту
    server.sendto(bytes(name, 'utf-8'), address)
