def skaiciuojam_iki2(_iter):
    a = "bla"
    while True:
        try:
            return next(_iter)
        except StopIteration:
            break


def skaiciuojam_iki(iki):
    count = 0
    while count < iki:
        yield count
        count += 1


iteratorius = iter(range(4))
skaiciuojam_iki2(iteratorius)
skaiciuojam_iki2(iteratorius)

generatorius = skaiciuojam_iki(4)
print(next(generatorius))
print("Nuo cia:")

for i in generatorius:
    print(i)

pass
