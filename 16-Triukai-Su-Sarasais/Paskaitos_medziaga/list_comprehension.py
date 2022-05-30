import math

sarasas = [4, 3, 2, 1, 11, 7, 8]
naujas = [x**2 for x in sarasas if x % 2 == 0]

rez = []
for elem in sarasas:
    if elem % 2 == 0:
        rez.append(elem ** 2)

pass
