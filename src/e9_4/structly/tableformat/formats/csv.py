from ..formatter import TableFormatter


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(map(str, rowdata)))


__all__ = ['CSVTableFormatter']
