# Brink Flair 300 Modbus control

## Ovladani rekuperacni jednotky Brink Flair 300 pres protokol Modbus

| Parametry spojeni    |                 |
|------------------------|-----------------|
| Protocol version:      | RTU             |
| Baudrate:              | 19k2 (19200 Bd) |
| Default slave address: | 20              |
| Parity:                | Even            |
| Stop bits:             | 1               |

##### Hardware:
Raspberry Pi Model 3B+

##### Operacni system:
https://www.openhab.org/docs/installation/openhabian.html \
Version: 2.5.10 (Build)

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

###### Informace o USB zarizenich:
    [00:06:29] openhabian@openHABianPi:~$ ll /dev | grep ttyUSB
    crw-rw----  1 root dialout 188,   0 Nov  7 00:06 ttyUSB0

    [23:28:58] openhabian@openHABianPi:~$ lsusb
    Bus 001 Device 009: ID 1a86:7523 QinHeng Electronics HL-340 USB-Serial adapter
    Bus 001 Device 004: ID 0424:7800 Standard Microsystems Corp.
    Bus 001 Device 003: ID 0424:2514 Standard Microsystems Corp. USB 2.0 Hub
    Bus 001 Device 002: ID 0424:2514 Standard Microsystems Corp. USB 2.0 Hub
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

Cesta `/dev/ttyUSB0` se pak pouziva jako device/port pro komunikaci pres Modbus.

##### Command line nastroj mbpoll:
https://github.com/epsilonrt/mbpoll

##### Python knihovna MinimalModbus:
https://minimalmodbus.readthedocs.io/en/master/readme.html

##### Specifikace prikazu:
 * https://www.storc.cz/wp-content/uploads/2018/11/Flair_325.pdf \
strana 53, spousta adres tam ale neni

 * https://www.brinkclimatesystems.nl/getattachment/ff69a0ac-80a3-4070-8731-8f70e8cca320

##### openHAB Modbus binding:
https://www.openhab.org/addons/bindings/modbus/

##### Implementace v openHAB pro jednotku Brink Renovent Excellent 300:
https://community.openhab.org/t/brink-renovent-excellent-300-air-ventilation-integration/91373/6

### Implementace

Cteni a zapis dat pres prikazovou radku pres nastroj [mbpoll](https://github.com/epsilonrt/mbpoll) je popsana v souboru [commands.md](commands.md).

Cteni dat v python skriptu prostrednictvim knihovny [MinimalModbus](https://minimalmodbus.readthedocs.io/en/master/readme.html) je v souboru [brink.py](brink.py).

Implementace v openHABu pres [Modbus Binding](https://www.openhab.org/addons/bindings/modbus/) (things, items, sitemap atd.) je v adresari [openhab](openhab).

Prehled hodnot pro cteni/zapis je v tabulce [properties.csv](properties.csv).
