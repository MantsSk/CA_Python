class Studentas:
    def __init__(self, vardas, amžius, lytis):
        self.vardas = vardas
        self.amžius = amžius
        self.lytis = lytis


class Kursas:
    def __init__(self, pavadinimas):
        self.pavadinimas = pavadinimas
        self.studentai = []

    def pridėti_studentą(self, studentas):
        self.studentai.append(studentas)


# Panaudojimas
kursas = Kursas("Informatika")

studentas1 = Studentas("Agnė", 20, "Moteris")
studentas2 = Studentas("Jonas", 22, "Vyras")

kursas.pridėti_studentą(studentas1)
kursas.pridėti_studentą(studentas2)

print("Kursas:", kursas.pavadinimas)
print("Studentai:", len(kursas.studentai))