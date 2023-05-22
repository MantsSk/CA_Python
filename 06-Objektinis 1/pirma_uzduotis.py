class Stačiakampis:
    def __init__(self, plotis, aukštis):
        self.plotis = plotis
        self.aukštis = aukštis

    def apskaičiuoti_plotą(self):
        return self.plotis * self.aukštis

    def apskaičiuoti_perimetrą(self):
        return 2 * (self.plotis + self.aukštis)


# Panaudojimas
stačiakampis = Stačiakampis(5, 10)
print("Plotas:", stačiakampis.apskaičiuoti_plotą())
print("Perimetras:", stačiakampis.apskaičiuoti_perimetrą())