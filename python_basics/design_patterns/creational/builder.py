class Director:
    def __init__(self, builder) -> None:
        self._builder = builder

    def create_car(self):
        self._builder.build_car()
        self._builder.add_name()
        self._builder.add_model()
        self._builder.add_engine_type()

    def get_car(self):
        return self._builder.car


class Builder:
    def __init__(self) -> None:
        self.car = None

    def build_car(self):
        self.car = Car()


class Hundai(Builder):

    def __init__(self) -> None:
        super().__init__()

    def add_name(self):
        self.car.name = "i20"

    def add_model(self):
        self.car.name = "Elite"

    def add_engine_type(self):
        self.car.engine_type = "Diesel"


class Car:
    def __init__(self) -> None:
        self.name = None
        self.model = None
        self.engine_type = None

    def __str__(self) -> str:
        return f"Car name : {self.name}, Model : {self.model}, Engine type : {self.engine_type}"


i20 = Hundai()
car = Director(i20)
car.create_car()
c = car.get_car()
print(c)
