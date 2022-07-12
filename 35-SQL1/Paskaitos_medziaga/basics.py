import sqlite3

conn = sqlite3.connect("../darbuotojai.db")

c = conn.cursor()

with conn:
    c.execute("""CREATE TABLE IF NOT EXISTS
    vadovai (
    vardas text,
    pavarde text,
    atlyginimas integer,
    skyrius text
    )""")

    c.execute(f"INSERT INTO vadovai VALUES ('x, y, z')")

    c.execute(f"SELECT * FROM vadovai WHERE vardas='z'")
    a = c.fetchall()

    pass
