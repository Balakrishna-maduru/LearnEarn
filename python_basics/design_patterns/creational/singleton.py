class Borg:
    _shares_data = {}

    def __init__(self) -> None:
        self.__dict__ = self._shares_data

#<--                      members example                       -->#


class Singleton(Borg):

    def __init__(self, **kvargs) -> None:
        super().__init__()
        self._shares_data.update(kvargs)

    def __str__(self) -> str:
        return str(self._shares_data)


http = Singleton(http="http://")
print(http)
https = Singleton(https="https://")
print(https)


class DataStore:
    _shared_data = {"members": []}

    def __init__(self):
        self.__dict__ = self._shared_data


class Singleton(DataStore):

    def __init__(self, **kvargs):
        DataStore.__init__(self)
#        self.__shared_data.update(kvargs)

    @property
    def mem(self):
        return list(self._shared_data["members"])

    @mem.setter
    def mem(self, name):
        members = self._shared_data["members"]
        members.append(name)
        self._shared_data["members"] = members


if __name__ == "__main__":
    s = Singleton()
    s.mem = "a"
    print(s.mem)
    s2 = Singleton()
    s2.mem = "b"
    print(s2.mem)
