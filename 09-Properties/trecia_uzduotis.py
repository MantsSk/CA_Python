

class Studentas:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits

    @property
    def credits(self):
        return self._credits

    @credits.setter
    def credits(self, credits_value):
        if credits_value > 30:
            self._credits = 30
        elif credits_value < 0:
            self._credits = 0
        else:
            self._credits = credits_value

    def print_info(self):
        print(f"Name is {self.name} and the person has {self.credits} credits")

s = Studentas("Mantas", -5)
s.print_info()

s2 = Studentas("Juozas", 22)
s2.print_info()

s3 = Studentas("Rokas", 36)
s3.print_info()
