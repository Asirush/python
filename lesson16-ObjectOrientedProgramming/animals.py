class Legs:
    def __init__(self, legs: int) -> None:
        self.legs = legs

class Animal:
    def __init__(self, sound: str, show: str, type: str, legs: int) -> None:
        self.Sound = sound
        self.Show = show
        self.Type = type
        self.Legs = legs

    def sound(self):
        print(self.Sound)

    def show(self):
        print(self.Show)

    def type(self):
        print(self.Type)

    def legs(self):
        print(self.legs)

if __name__ == "__main__":
    humster = Animal(sound="pi-pi-pi", show="Businka", type="Rodents")
    cat = Animal(sound="meow", show="Snowy", type="Felis")
    humster.sound()
    cat.sound()