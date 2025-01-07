import csv
from pathlib import Path


class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares = self.shares - nshares if nshares < self.shares else 0


def read_portfolio(path):
    portfolio = []
    with open(path, 'r') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            portfolio.append(Stock(row[0], int(row[1]), float(row[2])))
    return portfolio


def print_portfolio(portfolio):
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))


if __name__ == '__main__':
    s = Stock('GOOG', 100, 490.10)
    print(s.shares)
    s.sell(25)
    print(s.shares)
    path = Path(__file__).parent / '../..' / 'Data/portfolio.csv'
    portfolio = read_portfolio(path)
    print_portfolio(portfolio)
