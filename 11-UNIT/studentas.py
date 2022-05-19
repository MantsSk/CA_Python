
class Studentas:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits

    @property
    def credits(self):
        return self.__credits

    @credits.setter
    def credits(self, credits_value):
        if credits_value > 30:
            self.__credits = 30
        elif credits_value < 0:
            self.__credits = 0
        else:
            self.__credits = credits_value

    def print_info(self):
        print(f"Name is {self.name} and the person has {self.credits} credits")

