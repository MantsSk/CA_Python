class Parent:
    def __init__(self):
        self.appearance = "Public"
        self._riches = "Inherited by children"
        self.__memories = "Only private"

    def chant_in_a_protest(self):
        print("everyone can hear")

    def _talk_at_home(self):
        print("only children will hear")

    def __think(self):
        print("thoughts are only internal")


class Child(Parent):
    def __init__(self):
        super(Child, self).__init__()
        self.__memories = "Have to define my own"

