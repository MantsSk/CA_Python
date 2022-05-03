from sqlalchemy import true

skaicius_ne_nulis = true

try:
    while skaicius_ne_nulis:
        skaicius = int(input("Įveskite skaičių: "))
        skaicius_ne_nulis = bool(skaicius)
        print(skaicius_ne_nulis)
        if not skaicius_ne_nulis:
            break
except ValueError:
    print("Ivestas netinkamas skaicius")

# print("toliau")