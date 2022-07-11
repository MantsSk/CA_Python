import abc


class Animal(abc.ABC):

    @abc.abstractmethod
    def interact(self):
        pass


class Hamster(Animal):
     def interact(self):
        if self.mood < 60:
            print("Run away")
        else:
            print("Squeak")


class Cat(Animal):

    def __init__(self, mood, tail_len=20):
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


tom = Cat(20)
assert tom.tail_len == 30
jerry = Hamster()
giraff = Animal()
pass

len("abc")
len([1, 2, 3, 4])
