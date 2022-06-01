import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('dalyba.log')
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

def dalyba(a, b):
    try:
        rezultatas = a / b
    except ZeroDivisionError:
        logger.exception("Dalyba is nulio")
    else:
        logger.info(f"{a} padalinta is {b} lygu {rezultatas}")
        return rezultatas

dalyba(10,2)