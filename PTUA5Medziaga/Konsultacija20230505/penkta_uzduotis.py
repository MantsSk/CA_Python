knygos = {
    "Faustas": "Johanas Volfgangas Gėtė",
    "Knyga apie miškus": "Peteris Wohllebenas",
    "Karalius Lyras": "Williamas Shakespeare'as",
    "Idėjos": "Ray Dalio",
}
pavadinimas = input("Įveskite knygos pavadinimą: ")
if pavadinimas in knygos:
    print(knygos[pavadinimas])
else:
    print("Tokios knygos nėra")
