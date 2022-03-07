
from sqlite3 import converters
from unicodedata import decimal


class Converters:

    def __init__(self) -> None:
        pass

    def decimal_to_binary(self, number, out=''):
        if number >= 1:
            out = self.decimal_to_binary(number//2, out)
        return out + str(number % 2)

    def decimal_to_octa(self, number, out=''):
        if number >= 1:
            out = self.decimal_to_octa(number//8, out)
        return out + str(number % 8)

if __name__ == "__main__":
    c = Converters()
    print(c.decimal_to_octa(225))
    