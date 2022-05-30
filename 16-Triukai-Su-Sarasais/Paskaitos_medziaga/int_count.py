sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]

int_kiekis = sum([type(c) is int for c in sarasas])
print(int_kiekis)

# 4

str_kiekis = sum(type(c) is str for c in sarasas)
print(str_kiekis)

# 2
