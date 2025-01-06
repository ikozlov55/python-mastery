import collections
import csv
import tracemalloc
from pathlib import Path
from sys import intern


class DataCollection(collections.abc.Sequence):
    def __init__(self, headers, types):
        self.headers = headers
        self.types = types
        self.cols = []

    def __len__(self):
        return len(self.cols)

    def __getitem__(self, index):
        if isinstance(index, slice):
            data = DataCollection(self.headers, self.types)
            data.cols = self.cols[index]
            return data
        else:
            values = self.cols[index]
            return {name: func(val) for name, func, val in zip(self.headers, self.types, values)}

    def append(self, row):
        self.cols.append([func(val) for func, val in zip(self.types, row)])


def read_csv_as_columns(path, coltypes):
    with open(path, 'r') as file:
        rows = csv.reader(file)
        headers = next(rows)
        data = DataCollection(headers, coltypes)
        for row in rows:
            data.append(row)

    return data


tracemalloc.start()
path = Path(__file__).parent / '../..' / 'Data/ctabus.csv'
data = read_csv_as_columns(path, [intern, intern, str, int])
print(len(data))
print(data[0])
print(data[1])
print(data[2])
s = data[10:15]
print(len(s))
print(s[0])
print(s[1])
print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
