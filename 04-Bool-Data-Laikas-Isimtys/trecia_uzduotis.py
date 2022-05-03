import datetime
from typing import final

try:
    ivesta = input("Įveskite metus formatu (YYYY-MM-DD) ")
    ivesta_data = datetime.datetime.strptime(ivesta, "%Y-%m-%d")
    galutine_data = ivesta_data - datetime.timedelta(weeks = 14)
    print(galutine_data.strftime("%Y - %B - %d - %A"))
except:
    print("Pasirinkote negera forma ivedimui")
    print(datetime.datetime.now().strftime("%Y - %B - %d - %A"))
