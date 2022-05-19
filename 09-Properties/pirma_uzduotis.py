class Player:
    def __init__(self, name, lives):
        self.name = name
        self.lives = lives

    def hit(self):
        self.lives -= 1

    @property
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self, lives_value):
        self._lives = lives_value

    @property
    def is_alive(self):
        if self.lives > 0:
            return True

p = Player("Mantas", -1)
while True:
    if not p.is_alive:
        print(f"Veikejas {p.name} mire")
        break

    print(f"Gyvybes skaicius: {p.lives}")
    move = int(input("Parašykite 1 ir spustelkite enter, kad atimti vieną gyvybę "))
    if move == 1:
        p.hit()
    else:
        print("blogas pasirinkimas")
