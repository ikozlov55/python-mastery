from pathlib import Path

from structly.reader import read_csv_as_instances
from structly.structure import Structure
from structly.tableformat import create_formatter, print_table


class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares


if __name__ == '__main__':
    path = Path(__file__).parent / '../..' / 'Data/portfolio.csv'
    portfolio = read_csv_as_instances(path, Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name', 'shares', 'price'], formatter)
