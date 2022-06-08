import re

def date_format(date):
    pattern = re.compile(r'^(\d{2})\.(\d{2})\.(\d{4})$')
    res = pattern.sub('\g<3> \g<2> \g<1>', date)
    return res

print(date_format("22.11.2024"))

