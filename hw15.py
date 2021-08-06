# -*- coding: utf-8 -*-
import ipaddress


# Написать класс router.
# Должен иметь методы добавить/удалить/вывести список ip address.
# Должен иметь методы добавить/удалить/вывести список ip routes.
#
# Есть маршруты к непосредственно-подключенным сетям:
# если у устройства есть ip-adress 192.168.5.14/24 на интерфейсе eth1,
# значит у него должен быть маршрут:
# к сети 192.168.5.0/24 через eth1 или через 192.168.5.14.
#
# Если мы хотим добавить маршрут к какой-нибудь удаленной сети,
# то надо проверять доступен ли gateway.
#
# Например мы можем добавить маршрут к 172.16.0.0/16 через gateway
# 192.168.5.132, только если у нас уже есть маршрут до 192.168.5.132.
#
# Если же мы попытаемся добавить маршрут до какой-либо сети через gateway,
# до которого у нас пока еще нет маршрута, то должен вылетать exception.
#
# Например:
# Добавляем ip-address 192.168.5.14/24 eth1.
# Добавляем маршрут до 172.16.0.0/16 через 192.168.5.1 - ok.
# Добавляем маршрут до 172.24.0.0/16 через 192.168.8.1 - exception.
# Добавляем маршрут до 172.24.0.0/16 через 172.16.8.1 - ok.
#
# Итого - 1 интерфейс и 3 маршрута в таблице.

class Router():
    def __init__(self):
        self.rotes = {}
        self.ip_interfaces = {}

    def add_ip_address(self, ip_address, interface):
        '''Добавляет интерфейс и добавляет маршрут к сети за этим интерфейсовм'''
        ip_address = ipaddress.ip_interface(ip_address)
        self.ip_interfaces[ip_address] = interface
        self.rotes[ip_address.network] = ip_address.ip

    def delete_ip_address(self, ip_address):
        '''Удаляет интерфейс и маршруты, связанные с ним'''
        ip_address = ipaddress.ip_interface(ip_address)
        self.ip_interfaces.pop(ip_address)
        self.rotes.pop(ip_address.network)
        print(f'interface with ip {ip_address} was deleted')
        known_routes = [[net, gateway] for net, gateway in self.rotes.items()]
        for route in known_routes:
            if route[1] in ip_address.network:
                self.rotes.pop(route[0])
        self.check_dead_routes()

    def check_dead_routes(self):
        '''Проверяет наличие gateway в маршрутах, до которых нет маршрута. Если находит - удаляет их'''
        known_routes = [[net, gateway] for net, gateway in self.rotes.items()]
        for i_route in known_routes:
            check = 0
            for j_route in known_routes:
                if i_route[1] in j_route[0]:
                    check = 1
                if check == 0 and i_route[1] not in self.ip_interfaces:
                    self.rotes.pop(i_route[0])

    def export_ip_address(self):
        '''Выводит на консоль все интерфейсы, созданные на Router'''
        print(self.ip_interfaces)

    def add_ip_route(self, network, gateway):
        '''Добавляет маршрут до network через указаный gateway, если у нас нет маршрута до gateway, то маршрут не
        добавится'''
        known_routes = [net for net in self.rotes.keys()]
        for net in known_routes:
            if ipaddress.ip_address(gateway) in net:
                self.rotes[ipaddress.ip_network(network)] = ipaddress.ip_address(gateway)
                print(f'route to {ipaddress.ip_network(network)} was added')
                return
        print(f'can not find route to {ipaddress.ip_address(gateway)}')

    def delete_ip_routes(self, network):
        '''Удаляет указанную network из маршрутов, маршрутов к этой сети нет-выведет exception'''
        if ipaddress.ip_network(network) in self.rotes:
            self.rotes.pop(ipaddress.ip_network(network))
            print(f'route to {ipaddress.ip_network(network)} was deleted')
        else:
            print(f'can not find route to {ipaddress.ip_network(network)}')

    def export_ip_routes(self):
        '''Выводит на консоль все маршруты, созданные на Router'''
        print(self.rotes)


my_router = Router()

my_router.add_ip_address('192.168.5.14/24', 'eth1')

my_router.add_ip_route('172.16.0.0/16', '192.168.5.1')

my_router.add_ip_route('172.24.0.0/16', '192.168.8.1')

my_router.add_ip_route('172.24.0.0/16', '172.16.8.1')

my_router.export_ip_address()
my_router.export_ip_routes()

my_router.delete_ip_routes('172.24.0.0/16')
my_router.export_ip_routes()

my_router.add_ip_address('172.24.0.15/16', 'eth2')

my_router.delete_ip_address('192.168.5.14/24')

my_router.export_ip_address()
my_router.export_ip_routes()
