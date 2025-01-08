import csv
import logging
from pathlib import Path


def csv_as_dicts(lines, types, headers=None):
    '''
    Convert lines of CSV data into a list of dictionaries
    '''

    def make_records(headers, row):
        return {name: func(val)
                for name, func, val in zip(headers, types, row)}

    return convert_csv(lines, make_records, headers)


def make_dict(headers, row):
    return dict(zip(headers, row))


def convert_csv(lines, func, headers=None):
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    records = []
    for i, row in enumerate(rows):
        try:
            records.append(func(headers, row))
        except ValueError as e:
            logging.warning(f'Row {i + 1}: Bad row: {row}')
            logging.debug(f'Reason: {e}')
    return records


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    path = Path('../../Data/missing.csv')
    with open(path, 'r') as file:
        lines = file.readlines()
        for record in csv_as_dicts(lines, types=[str, int, float]):
            print(record)
