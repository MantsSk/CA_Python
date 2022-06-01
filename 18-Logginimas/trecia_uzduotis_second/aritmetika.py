import math
import dalyba


import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('aritmetika.log')
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

def suma(*args):
    logging.info(f"Skaiciu {args} suma lygi: {sum(args)}")
    return sum(args)

def saknis(x):
    try:
        rezultatas = math.sqrt(x)
    except TypeError:
        logger.exception("Saknis gali buti traukiama tik is skaiciaus")
    else:
        logger.info(f"Skaiciaus {x} saknis lygi {rezultatas}")
        return rezultatas

def simboliai(sakinys):
    logging.info(f"Sakinio {sakinys} ilgis lygus {len(sakinys)} simboliu")
    return len(sakinys)


print(suma(4, 5, 7, 8, 9, 9))
print(saknis("Donatas"))
print(simboliai("Labas vakaras"))
