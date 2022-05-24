import sqlite3

# conn = sqlite3.connect("../darbuotojai.db")
conn = sqlite3.connect(":memory:")

c = conn.cursor()

class Darbuotojas:
    def __init__(self, name, surname, salary, department):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.department = department

domas = Darbuotojas("Domas'; DROP ALL TABLES;", "Petrauskas", 1500, "sandeliavimas")


with conn:
    c.execute("""CREATE TABLE IF NOT EXISTS
    vadovai (
    vardas text,
    pavarde text,
    atlyginimas integer,
    skyrius text
    )""")

    c.execute(f"INSERT INTO vadovai VALUES ('{domas.name}', '{domas.surname}', {domas.salary}, '{domas.department}')")

    c.execute(f"SELECT * FROM vadovai WHERE vardas='{domas.name}'")
    a = c.fetchall()

    pass
