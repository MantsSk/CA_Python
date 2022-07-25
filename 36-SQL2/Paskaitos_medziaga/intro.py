import sqlite3
from sqlite3 import OperationalError

conn = sqlite3.connect("darbuotojai.db")
c = conn.cursor()

try:
    with conn:
        c.execute("DELETE FROM neesanti_lentele where vardas=\"vakaris\" ")
        print(c.fetchone())
except OperationalError as e:
    print(f"Nepavyko isstrinti: {e}")
