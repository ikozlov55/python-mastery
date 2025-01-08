import csv
from pathlib import Path


def csv_as_dicts(lines, types, headers=None):
    '''
    Convert lines of CSV data into a list of dictionaries
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = {name: func(val)
                  for name, func, val in zip(headers, types, row)}
        records.append(record)
    return records


def csv_as_instances(lines, cls, headers=None):
    '''
    Convert lines of CSV data into a list of instances
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records


def make_dict(headers, row):
    return dict(zip(headers, row))


def convert_csv(lines, func, *args, headers=None):
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    return list(map(lambda r: func(headers, r, *args), rows))


if __name__ == '__main__':
    path = Path('../../Data/portfolio.csv')
    with open(path, 'r') as file:
        lines = file.readlines()
        records = convert_csv(lines, make_dict)
        print(records)
