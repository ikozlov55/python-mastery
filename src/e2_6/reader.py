import csv
import tracemalloc
from pathlib import Path
from sys import intern


def read_csv_as_dicts(path, coltypes):
    records = []
    with open(path, 'r') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = {name: func(val) for name, func, val in zip(headers, coltypes, row)}
            records.append(record)
    return records


path = Path(__file__).parent / '../..' / 'Data/portfolio.csv'
portfolio = read_csv_as_dicts(path, [str, int, float])
for s in portfolio:
    print(s)

tracemalloc.start()
path = Path(__file__).parent / '../..' / 'Data/ctabus.csv'
rows = read_csv_as_dicts(path, [intern, intern, str, int])
print(len(rows))
print(rows[0])
routeids = {id(row['route']) for row in rows}
print(len(routeids))
print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())



