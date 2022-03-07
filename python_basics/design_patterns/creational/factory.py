class Dog:
    def __init__(self):
        self.pet_type = "Dog"
        self._speak = "Bow..!"
        self._food = "Bones..!"

    def speak(self):
        print(f"{self.pet_type} speaks -> {self._speak}")

    def food(self):
        print(f"{self.pet_type} eats -> {self._food}")


class Cat:
    def __init__(self):
        self.pet_type = "Cat"
        self._speak = "Meaw..!"
        self._food = "mouse..!"

    def speak(self):
        print(f"{self.pet_type} speaks -> {self._speak}")

    def food(self):
        print(f"{self.pet_type} eats -> {self._food}")


class pet_store:
    def __init__(self) -> None:
        self.pets = {"Dog": Dog(), "Cat": Cat()}

    def get_pet(self, pet="Dog"):
        return self.pets.get(pet)


p = pet_store()
d = p.get_pet()
d.speak()
d.food()
c = p.get_pet("Cat")
c.speak()
c.food()
