import os
from datetime import datetime


katalago_pavadinimas = "Naujas Katalogas"
failo_pavadinimas = "data.txt"

os.chdir('../')
os.mkdir(katalago_pavadinimas)
os.chdir(katalago_pavadinimas)


with open(failo_pavadinimas, "w") as failas:
    failas.write(str(datetime.today())+ "\n")
    failas.write(str(os.getcwd()))

print("Sukūrimo data:", datetime.fromtimestamp(os.stat("data.txt").st_ctime))
print("Failo dytis:", os.stat("data.txt").st_size)