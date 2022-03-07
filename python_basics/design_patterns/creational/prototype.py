import copy


class Prototype:
    def __init__(self) -> None:
        self.object_store = {}

    def register(self, name, object_to_store) -> None:
        self.object_store[name] = object_to_store

    def deregister(self, name) -> None:
        del self.object_store[name]

    def clone(self, name, **kvargs):
        object_to_clone = self.object_store.get(name)
        cloned_object = copy.deepcopy(object_to_clone)
        cloned_object.__dict__.update(kvargs)
        return cloned_object


class Car:
    def __init__(self) -> None:
        self.name = "Hundai"
        self.model = "i20"
        self.m_year = "2017"

    def __str__(self) -> str:
        return f"company : {self.name}, model : {self.model}, manufactring year : {self.m_year}"


i20_2017 = Car()
prototype = Prototype()
prototype.register('i20_2017', i20_2017)
i20_2022 = prototype.clone('i20_2017', m_year=2022)
print(i20_2017)
print(i20_2022)
