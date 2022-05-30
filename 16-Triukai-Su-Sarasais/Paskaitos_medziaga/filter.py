sarasas = [4, 3, 2, 1]

def daugiau_nei_2(sarasas):
    sarasas_2 = []
    for skaicius in sarasas:
        if skaicius > 2:
            sarasas_2.append(skaicius)
    return sarasas_2

print(daugiau_nei_2(sarasas))


isfiltruotas = list(filter(lambda x: not x > 2, sarasas))
pass
