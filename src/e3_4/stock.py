from decimal import Decimal


class Stock:
    __slots__ = ['name', '_shares', '_price']
    _types = (str, int, float)

    def __init__(self, name, shares, price):
        self.name = name
        self._shares = shares
        self._price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        t = self._types[1]
        if not isinstance(value, t):
            raise ValueError(f'Expected {t.__name__}')
        if value < 0:
            raise ValueError('shares must be >= 0')
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        t = self._types[2]
        if not isinstance(value, t):
            raise ValueError(f'Expected {t.__name__}')
        if value < 0:
            raise ValueError('rice must be >= 0')
        self._price = value

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares = self.shares - nshares if nshares < self.shares else 0

    @classmethod
    def from_row(cls, row):
        return cls(*[func(val) for func, val in zip(cls._types, row)])


class DStock(Stock):
    _types = (str, int, Decimal)


if __name__ == '__main__':
    s = Stock('GOOG', 100, 490.10)
    s.shares = 50
    s.price = 120.5
    print(s.name)
    print(s.shares)
    print(s.price)
    print(s.cost)
    print()

    d = DStock('GOOG', 100, 490.10)
    d.shares = 50
    d.price = Decimal(120.5)
    print(d.name)
    print(d.shares)
    print(d.price)
    print(d.cost)
