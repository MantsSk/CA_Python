sarasas = [4, 3, 2, 1]

sarasas_2 = []
for skaicius in sarasas:
    sarasas_2.append(skaicius ** 2)

print(sarasas_2)

# [16, 9, 4, 1]
# SU map

def kvadratu(skaicius):
    return skaicius ** 2

sar3 = list(map(lambda x: x ** 2, sarasas))

pass

