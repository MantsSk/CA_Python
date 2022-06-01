import math
import logging
import dalyba


logging.basicConfig(filename="aritmetika.log", level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def suma(*args):
    logging.info(f"Skaiciu {args} suma lygi: {sum(args)}")
    return sum(args)

def saknis(x):
    try:
        rezultatas = math.sqrt(x)
    except TypeError:
        logging.exception("Saknis gali buti traukiama tik is skaiciaus")
    else:
        logging.info(f"Skaiciaus {x} saknis lygi {rezultatas}")
        return rezultatas

def simboliai(sakinys):
    logging.info(f"Sakinio {sakinys} ilgis lygus {len(sakinys)} simboliu")
    return len(sakinys)


print(suma(4, 5, 7, 8, 9, 9))
print(saknis("Donatas"))
print(simboliai("Labas vakaras"))
