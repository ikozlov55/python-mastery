from abc import ABC, abstractmethod


class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        raise NotImplementedError()


class ColumnFormatMixin:
    formats = []

    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)


class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-' * 10 + ' ') * len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))


class PortfolioFormatter(ColumnFormatMixin, UpperHeadersMixin, TextTableFormatter):
    formats = ['%s', '%d', '%0.2f']


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
    if not isinstance(formatter, TableFormatter):
        raise TypeError('Expected TableFormatter!')
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)


def create_formatter(format, column_formats=None, upper_headers=False):
    match format:
        case 'text':
            base = TextTableFormatter()
        case 'csv':
            base = CSVTableFormatter()
        case 'html':
            base = HTMLTableFormatter()
        case _:
            raise AttributeError('Unknown formats!')
    mixins = []
    if column_formats:
        mixins.append(ColumnFormatMixin)
    if upper_headers:
        mixins.append(UpperHeadersMixin)
    if mixins:
        class CustomTableFormatter(*mixins, base.__class__):
            pass

        base = CustomTableFormatter()
        base.formats = column_formats
    return base
