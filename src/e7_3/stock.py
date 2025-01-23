from structure import Structure
from validate import String, PositiveInteger, PositiveFloat


class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares = self.shares - nshares if nshares < self.shares else 0

    @classmethod
    def from_row(cls, row):
        return cls(*[func(val) for func, val in zip((str, int, float), row)])


if __name__ == '__main__':
    s1 = Stock('GOOG', 100, 490.10)
    s1.price = 10.0
    s1.sell(50)
    s1.sell(-20)
    print(s1)
    s2 = Stock.from_row(['GOOG', '100', '490.1'])
    print(s2.price)
    print(s2)
