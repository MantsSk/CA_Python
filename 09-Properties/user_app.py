from antra_uzduotis import Person

p = Person("Mantas", "Skara")

p.name = "Tomas"
print(p.fullname)
print(p.email())
# p.fullname = "Juozas" # can't set attribute 'fullname'