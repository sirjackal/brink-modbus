## Cteni a zapis hodnot 

##### Teplota privodniho vzduchu (stupne C, vydelit 10):
    mbpoll -a 20 -b 19200 -r 4036 -t 3 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0

##### Teplota odpadniho vzduchu (stupne C, vydelit 10):
    mbpoll -a 20 -b 19200 -r 4046 -t 3 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0

##### Venkovni teplota (stupne C, vydelit 10):
     mbpoll -a 20 -b 19200 -r 4081 -t 3 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0

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
    mbpoll -a 20 -b 19200 -r 6100 -t 4 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0

    # 0: Automatický 1: Uzavřený obtok 2: Otevřený obtok

##### Bypass - min. teplota uvnitr:
    mbpoll -a 20 -b 19200 -r 6101 -t 4 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0    

##### Bypass - min. teplota venku:
    mbpoll -a 20 -b 19200 -r 6102 -t 4 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0        

##### Bypass - hystereze:
    mbpoll -a 20 -b 19200 -r 6103 -t 4 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0        

##### Bypass - boost:
    mbpoll -a 20 -b 19200 -r 6104 -t 4 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0        

    # 0: vypnutý 1: zapnutý

##### Bypass - stupen vykonu pri boostu:
    mbpoll -a 20 -b 19200 -r 6105 -t 4 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0        

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

##### Prutok na jednotlive stupne:
    # stupen 0 (nepritomnost):
    mbpoll -a 20 -b 19200 -r 6000 -t 4 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0

    # stupen 1 (nizky):
    mbpoll -a 20 -b 19200 -r 6001 -t 4 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0

    # stupen 2 (stredni):
    mbpoll -a 20 -b 19200 -r 6002 -t 4 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0

    # stupen 3 (vysoky):
    mbpoll -a 20 -b 19200 -r 6003 -t 4 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0

##### Vlhkost vzduchu na vstupu:
    mbpoll -a 20 -b 19200 -r 4037 -t 3 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0

##### Vlhkost vzduchu na vystupu:
    mbpoll -a 20 -b 19200 -r 4047 -t 3 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0    

##### Pouziti filtru v hodinach
    mbpoll -a 20 -b 19200 -r 4115 -t 3 -c 1 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0 

##### Požadované nastavení průtoku vzduchu:
    mbpoll -a 20 -b 19200 -r 8002 -t 4 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0 200

    # 0; 50–325
    # Ovládání ModBus je nutné nastavit na 2 (hodnota průtoku)

##### Výstraha resetování filtru:
    mbpoll -a 20 -b 19200 -r 8010 -t 4 -v -m rtu -d 8 -p even -1 -0 /dev/ttyUSB0 1

    # 0: Bez resetu 1: Výstraha resetování filtru
