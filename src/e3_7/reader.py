import csv
from abc import ABC, abstractmethod
from pathlib import Path

from src.e3_6.stock import Stock


class CSVParser(ABC):

    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records

    @abstractmethod
    def make_record(self, headers, row):
        pass


class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types

    def make_record(self, headers, row):
        return {name: func(val) for name, func, val in zip(headers, self.types, row)}


class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls

    def make_record(self, headers, row):
        return self.cls.from_row(row)


def read_csv_as_dicts(path, coltypes):
    parser = DictCSVParser(coltypes)
    return parser.parse(path)


def read_csv_as_instances(path, cls):
    parser = InstanceCSVParser(cls)
    return parser.parse(path)


if __name__ == '__main__':
    path = Path(__file__).parent / '../..' / 'Data/portfolio.csv'
    for s in read_csv_as_dicts(path, [str, int, float]):
        print(s)

    for s in read_csv_as_instances(path, Stock):
        print(s)
