from structure import Structure


class Stock(Structure):
    def __init__(self, name, shares, price):
        self._init()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares


Stock.set_fields()

if __name__ == '__main__':
    s = Stock(name='GOOG', price=490.1, shares=50)
    print(s.name)
    print(s.shares)
    print(s.price)
    print(repr(s))
