def kartojimas(kartai):
    def kartoti(fn):
        def wrapper():
            for i in range(kartai):
                fn()
        return wrapper
    return kartoti

@kartojimas(kartai=3)
def spausdinti_teksta():
    print("Spausdinamas tekstas!")


spausdinti_teksta()