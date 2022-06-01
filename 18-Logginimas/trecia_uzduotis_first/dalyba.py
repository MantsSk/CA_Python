import logging

logging.basicConfig(filename='dalyba.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

def dalyba(a, b):
    try:
        rezultatas = a / b
    except ZeroDivisionError:
        logging.exception("Dalyba is nulio")
    else:
        logging.info(f"{a} padalinta is {b} lygu {rezultatas}")
        return rezultatas

dalyba(10,2)