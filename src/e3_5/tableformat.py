from pathlib import Path

from src.e3_1.stock import read_portfolio


class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-' * 10 + ' ') * len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(map(str, rowdata)))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join(['<tr>', *(f'<th>{h}</th>' for h in headers), '</tr>']))

    def row(self, rowdata):
        print(' '.join(['<tr>', *(f'<td>{r}</td>' for r in rowdata), '</tr>']))


def print_table(records, fields, formatter):
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)


def create_formatter(format):
    match format:
        case 'text':
            return TextTableFormatter()
        case 'csv':
            return CSVTableFormatter()
        case 'html':
            return HTMLTableFormatter()
        case _:
            raise AttributeError('Unknown formats!')

if __name__ == '__main__':
    path = Path(__file__).parent / '../..' / 'Data/portfolio.csv'
    portfolio = read_portfolio(path)
    print_table(portfolio, ['name', 'shares', 'price'], create_formatter('text'))
    print()
    print_table(portfolio, ['name', 'shares', 'price'], create_formatter('csv'))
    print()
    print_table(portfolio, ['name', 'shares', 'price'], create_formatter('html'))
