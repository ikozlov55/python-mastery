from abc import ABC, abstractmethod


class TableFormatter(ABC):
    _formats = {}

    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        raise NotImplementedError()

    @classmethod
    def __init_subclass__(cls):
        name = cls.__module__.split('.')[-1]
        TableFormatter._formats[name] = cls


class ColumnFormatMixin:
    formats = []

    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)


class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])


def print_table(records, fields, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError('Expected TableFormatter!')
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)


def create_formatter(name, column_formats=None, upper_headers=False):
    if name not in TableFormatter._formats:
        __import__(f'{__package__}.formats.{name}')
    formatter_cls = TableFormatter._formats.get(name)
    if not formatter_cls:
        raise RuntimeError('Unknown format %s' % name)

    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
            formats = column_formats

    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()


__all__ = ['create_formatter', 'print_table']
