class Animal:
    def __init__(self, mood=50):
        self._mood = mood

    def pet(self):
        self._alter_mood(10)

    def interact(self):
        raise NotImplementedError


class Hamster(Animal):
    pass
    #def interact(self):
    #    if self.mood < 60:
    #        print("Run away")
    #    else:
    #        print("Squeak")


class Cat(Animal):

    def __init__(self, mood=20, tail_len=20):
        super().__init__(mood)
        self.tail_len = tail_len

    def step_on_tail(self):
        self._alter_mood(-10 * self.tail_len)

    def interact(self):
        if self._mood < 50:
            print("HissSSss")
        else:
            print("Miau")

    def _alter_mood(self, change: int):
        self._mood += change

tom = Cat()
jerry = Hamster()


