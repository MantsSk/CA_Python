zodziai = []

zodziukiekis = int(input("Įveskite žodžių kiekį : "))

while len(zodziai) < zodziukiekis:
    ivedimas = (input("Įveskite žodį: "))
    if ivedimas == "":
        break
    zodziai.append(ivedimas)

for numeris, zodis in enumerate(zodziai):
    print(f"{numeris + 1}: {zodis}, simbolių kiekis: {len(zodis)}")
print("Žodžių kiekis:", len(zodziai))