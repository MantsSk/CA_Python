pilnas_zodis = "Tomas Juknevicius"

# print(vardas)
# print(vardas[-1])
# print(vardas[0])
vardas = pilnas_zodis[0:pilnas_zodis.find(" ")]
print(vardas)
pavarde = pilnas_zodis[pilnas_zodis.find(" ")+1:]
print(pavarde)
print(pilnas_zodis.upper())
print(pilnas_zodis[::-1])
print(pilnas_zodis.split())
print(pilnas_zodis.replace(pavarde, "Python Specialistas"))