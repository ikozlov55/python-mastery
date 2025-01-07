from pathlib import Path

from src.e3_1.stock import read_portfolio


def print_table(objs, attrs):
    result = ' '.join('%10s' % attr for attr in attrs) + '\n'
    result += ' '.join('-' * 10 for _ in attrs) + '\n'
    for o in objs:
        result += ' '.join('%10s' % getattr(o, attr) for attr in attrs) + '\n'
    print(result)


path = Path(__file__).parent / '../..' / 'Data/portfolio.csv'
portfolio = read_portfolio(path)
print_table(portfolio, ['name', 'shares', 'price'])
print()
print_table(portfolio, ['shares', 'name'])
