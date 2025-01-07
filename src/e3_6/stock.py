import sys
from pathlib import Path

from src.e3_1.stock import read_portfolio
from src.e3_5.tableformat import create_formatter


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

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self._shares}, {self._price})'

    def __eq__(self, other):
        return isinstance(other, self.__class__) and ((self.name, self.shares, self.price) ==
                                                      (other.name, other.shares, other.price))


class redirect_stdout:
    def __init__(self, out_file):
        self.out_file = out_file

    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self.out_file
        return self.out_file

    def __exit__(self, ty, val, tb):
        sys.stdout = self.stdout


def print_table(records, fields, formatter):
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)


if __name__ == '__main__':
    a = Stock('GOOG', 100, 490.10)
    print(repr(a))
    b = Stock('GOOG', 100, 490.10)
    print(repr(b))

    with redirect_stdout(open('out.txt', 'w')) as file:
        path = Path(__file__).parent / '../..' / 'Data/portfolio.csv'
        portfolio = read_portfolio(path)
        print_table(portfolio, ['name', 'shares', 'price'], create_formatter('csv'))
        file.close()
