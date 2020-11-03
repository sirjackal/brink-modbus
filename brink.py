#!/usr/bin/env python3

import minimalmodbus

instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 20)  # port name, slave address (in decimal)

instrument.serial.baudrate = 19200 # Baud
instrument.serial.bytesize = 8
instrument.serial.parity = minimalmodbus.serial.PARITY_EVEN
instrument.serial.stopbits = 1
instrument.serial.timeout = 0.5 # seconds
instrument.mode = minimalmodbus.MODE_RTU # rtu or ascii mode
instrument.clear_buffers_before_each_transaction = True

value = instrument.read_register(8001, 0, 3, False)  # Registernumber, number of decimals, function code
switchPositionEnum = { 0: 'nepritomnost', 1: 'nizke', 2: 'normalni', 3: 'vysoke' }
print('Stupen vykonu:', value, '(' + switchPositionEnum[value] + ')')

value = instrument.read_register(4036, 0, 4, True)  # Registernumber, number of decimals, function code
print('Privodni teplota:', value / 10, 'C')

value = instrument.read_register(4046, 0, 4, True)
print('Odvodni teplota:', value / 10, 'C')

value = instrument.read_register(4023, 0, 4, False)
print('Vstupni tlak:', value / 10, 'Pa')

value = instrument.read_register(4024, 0, 4, False)
print('Vystupni tlak:', value / 10, 'Pa')

value = instrument.read_register(4031, 0, 4, False)
print('Nastaveny vstupni objem vzduchu:', value, 'm3')

value = instrument.read_register(4032, 0, 4, False)
print('Aktualni vstupni objem vzduchu:', value, 'm3')

value = instrument.read_register(4041, 0, 4, False)
print('Nastaveny vystupni objem vzduchu:', value, 'm3')

value = instrument.read_register(4042, 0, 4, False)
print('Aktualni vystupni objem vzduchu:', value, 'm3')

value = instrument.read_register(6100, 0, 3, False)
bypassModeEnum = { 0: 'automaticky', 1: 'uzavreny', 2: 'otevreny' }
print('Rezim bypassu:', bypassModeEnum[value])

value = instrument.read_register(4050, 0, 4, False)
bypassStateEnum = { 0: 'inicializovat', 1: 'otevreny', 2: 'zavreny', 3: 'otevreny', 4: 'zavreny', 255: 'chyba' }
print('Stav bypassu:', bypassStateEnum[value])

value = instrument.read_register(4100, 0, 4, False)
filterStateEnum = { 0: 'cisty', 1: 'spinavy' }
print('Stav filtru:', filterStateEnum[value])

value = instrument.read_register(4060, 0, 4, False)
preheaterStateEnum = { 0: 'inicializovat', 1: 'neaktivni', 2: 'aktivni', 3: 'testovaci rezim' }
print('Stav predehrivace:', preheaterStateEnum[value])

value = instrument.read_register(4060, 0, 4, False)
print('Vykon predehrivace:', value, '%')

value = instrument.read_register(6033, 0, 3, False)
imbalanceEnum = { 0: 'nepovolena', 1: 'povolena' }
print('Nevyvazenost:', imbalanceEnum[value])

value = instrument.read_register(6035, 0, 3, False)
print('Odchylka nevyvazenosti privodu:', value, '%')

value = instrument.read_register(6036, 0, 3, False)
print('Odchylka nevyvazenosti odvodu:', value, '%')