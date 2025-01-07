import csv
from decimal import Decimal
from pathlib import Path


class Stock:
    types = (str, int, float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares = self.shares - nshares if nshares < self.shares else 0

    @classmethod
    def from_row(cls, row):
        return cls(*[func(val) for func, val in zip(cls.types, row)])


class DStock(Stock):
    types = (str, int, Decimal)


def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records


def print_portfolio(portfolio):
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))


if __name__ == '__main__':
    s = Stock('GOOG', 100, 490.10)
    print(s.name)
    print(s.shares)
    print(s.price)
    print(s.cost())
    print()
    s = DStock('GOOG', 100, 490.10)
    print(s.name)
    print(s.shares)
    print(s.price)
    print(s.cost())
    path = Path(__file__).parent / '../..' / 'Data/portfolio.csv'
    portfolio = read_csv_as_instances(path, DStock)
    print_portfolio(portfolio)
