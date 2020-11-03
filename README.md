# Brink Flair 300 Modbus control

##### Hardware:
Raspberry Pi Model 3B+

##### Operacni system:
https://www.openhab.org/docs/installation/openhabian.html

    [14:48:16] openhabian@openHABianPi:~/bin$ lsb_release -a
    No LSB modules are available.
    Distributor ID: Raspbian
    Description:    Raspbian GNU/Linux 9.8 (stretch)
    Release:        9.8
    Codename:       stretch
    
    [14:54:40] openhabian@openHABianPi:~/bin$ hostnamectl
       Static hostname: openHABianPi
             Icon name: computer
            Machine ID: e278d9daa394410b8bcf44d5cbf0d734
               Boot ID: 95082e508e5047f8a7b7f52461d7139b
      Operating System: Raspbian GNU/Linux 9 (stretch)
                Kernel: Linux 4.14.98-v7+
          Architecture: arm

##### Pouzity prevodnik:
https://arduino-shop.cz/arduino/1171-prevodnik-usb-na-rs485-chip-ch340c.html

##### Informace o USB zarizenich:
    lsusb

##### Command line nastroj mbpoll:
https://github.com/epsilonrt/mbpoll

##### Python knihovna MinimalModbus:
https://minimalmodbus.readthedocs.io/en/master/readme.html

##### Specifikace prikazu:
https://www.storc.cz/wp-content/uploads/2018/11/Flair_325.pdf \
strana 53

##### Implementace v openHAB:
https://community.openhab.org/t/brink-renovent-excellent-300-air-ventilation-integration/91373/6

## Cteni a zapis hodnot 

##### Privodni teplota (stupne C, vydelit 10):
    mbpoll -a 20 -b 19200 -r 4036 -t 3 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0

##### Odvodni teplota (stupne C, vydelit 10):
    mbpoll -a 20 -b 19200 -r 4046 -t 3 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0

##### Vstupni tlak (Pa, vydelit 10):
    mbpoll -a 20 -b 19200 -r 4023 -t 3 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0

##### Vystupni tlak (Pa, vydelit 10):
    mbpoll -a 20 -b 19200 -r 4024 -t 3 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0

##### Nastaveny vstupni objem vzduchu (m3):
    mbpoll -a 20 -b 19200 -r 4031 -t 3 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0

##### Aktualni vstupni objem vzduchu (m3):
    mbpoll -a 20 -b 19200 -r 4032 -t 3 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0

##### Nastaveny vystupni objem vzduchu (m3):
    mbpoll -a 20 -b 19200 -r 4041 -t 3 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0

##### Aktualni vystupni objem vzduchu (m3):
    mbpoll -a 20 -b 19200 -r 4042 -t 3 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0

##### Stav bypassu:
    mbpoll -a 20 -b 19200 -r 4050 -t 3 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0

    # 0: inicializovat / 1: otevřený / 2: zavřený / 3: otevřený / 4: zavřený / 255: chyba

##### Stav filtru:
    mbpoll -a 20 -b 19200 -r 4100 -t 3 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0

    # 0: není špinavý 1: špinavý

##### Stav predehrivace:
    mbpoll -a 20 -b 19200 -r 4060 -t 3 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0

    # 0: Inicializovat / 1: Neaktivní / 2: Aktivní / 3: Testovací režim

##### Vykon predehrivace (%):
    mbpoll -a 20 -b 19200 -r 4061 -t 3 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0

##### Nevyvazenost:
    mbpoll -a 20 -b 19200 -r 6033 -t 4 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0

    # 0: Nevyváženost nepovolena 1: nevyváženost povolena

##### Odchylka nevyvazenosti privodu:
    mbpoll -a 20 -b 19200 -r 6035 -t 4 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0

    # Hodnota je uvedena v procentech; 0 % znamená, že nebyla použita žádná korekce

##### Odchylka nevyvazenosti odvodu:
    mbpoll -a 20 -b 19200 -r 6036 -t 4 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0

    # Hodnota je uvedena v procentech; 0 % znamená, že nebyla použita žádná korekce

##### Rezim bypassu:
    mbpoll -a 20 -b 19200 -r 6100 -t 3 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0

    # 0: Automatický 1: Uzavřený obtok 2: Otevřený obtok

##### Ovládání ModBus:
    mbpoll -a 20 -b 19200 -r 8000 -t 4 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0 2
    
    # 0: Ovládání ModBus vypnuté 1: Ovládací spínač ModBus 2: Hodnota ovládání průtoku ModBus

##### Poloha spinace vykonu (cteni):
    mbpoll -a 20 -b 19200 -r 8001 -t 4 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0

    # 0: nepřítomnost 1: nízké 2: normální 3: vysoké

##### Navrhovaná změna polohy spínače výkonu (zapis):
    mbpoll -a 20 -b 19200 -r 8001 -t 4 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0 3

    # 0: nepřítomnost 1: nízké 2: normální 3: vysoké
    # Ovládání ModBus je nutné nastavit na 1 (přepínač)

##### Požadované nastavení průtoku vzduchu:
    mbpoll -a 20 -b 19200 -r 8002 -t 4 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0 200

    # 0; 50–325
    # Ovládání ModBus je nutné nastavit na 2 (hodnota průtoku)

##### Výstraha resetování filtru:
    mbpoll -a 20 -b 19200 -r 8010 -t 4 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0 1

    # 0: Bez resetu 1: Výstraha resetování filtru
