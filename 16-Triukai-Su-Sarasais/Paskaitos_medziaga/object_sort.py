class Atlyginimas:
    def __init__(self, bruto, neto):
        self.bruto = bruto
        self.neto = neto

class Darbuotojas:
    def __init__(self, vardas, pavarde, atlyginimas: Atlyginimas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.atlyginimas = atlyginimas

    def __repr__(self):
        return (f"({self.vardas}, {self.pavarde}, {self.atlyginimas})")

d1 = Darbuotojas("Tadas", "Rutkauskas", Atlyginimas(1500, 1300))
d2 = Darbuotojas("Domas", "Radzevičius", Atlyginimas(600, 1500))
d3 = Darbuotojas("Rokas", "Ramanauskas", Atlyginimas(1111, 1111))
sarasas = [d1, d2, d3]

def rusiavimas(darbuotojas):
    return darbuotojas.vardas

surusiuotas = sorted(sarasas, key=rusiavimas)
print(surusiuotas)

#[(Domas, Radzevičius, 2000), (Rokas, Ramanauskas, 1000), (Tadas, Rutkauskas, 1500)]

surusiuotas = sorted(sarasas, key=lambda e: e.atlyginimas.neto)
print(surusiuotas)

# [(Rokas, Ramanauskas, 1000), (Tadas, Rutkauskas, 1500), (Domas, Radzevičius, 2000)]

from operator import attrgetter
surusiuotas = sorted(sarasas, key=attrgetter("atlyginimas"))
print(surusiuotas)
