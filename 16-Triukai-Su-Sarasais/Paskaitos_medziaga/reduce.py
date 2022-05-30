from functools import reduce

sarasas = [4, 3, 2, 1]
naujas = reduce(lambda x, y: x + y, sarasas)
print(naujas)

# 10
result = 0
x = sarasas[0]

for i in range(0, len(sarasas) - 1):
    y = sarasas[i + 1]
    x = x + y
pass
