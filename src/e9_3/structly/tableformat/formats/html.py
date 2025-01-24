from ..formatter import TableFormatter


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join(['<tr>', *(f'<th>{h}</th>' for h in headers), '</tr>']))

    def row(self, rowdata):
        print(' '.join(['<tr>', *(f'<td>{r}</td>' for r in rowdata), '</tr>']))


__all__ = ['HTMLTableFormatter']
