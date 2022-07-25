import sqlite3

conn = sqlite3.connect("zmones.db")
c = conn.cursor()

draugai = [
    ('Jonas', 'Jonaitis', 'jjonaitis@mail.lt'),
    ('Petras', 'Miltelis', 'petras@pastas.lt'),
    ('Inga', 'Guobytė', 'ingag@koksskirtumas.lt')
]

vardai = [
    tuple(['Jonas']),
    tuple(['Petras']),
    tuple(['Inga']),
]

with conn:
    c.executemany("SELECT * FROM draugai where f_name=?", vardai)
    print(c.fetchall())
