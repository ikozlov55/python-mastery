from pathlib import Path
from typing import Optional

from src.e4_3.validate import Stock


def read_csv_as_dicts(filename: str, types: list,
                      headers: Optional[str] = None) -> list[dict]:
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    with open(filename) as file:
        lines = file.readlines()
        return csv_as_dicts(lines, types, headers)


def read_csv_as_instances(filename: str, cls: object,
                          headers: bool = False) -> list[object]:
    '''
    Read CSV data into a list of instances
    '''
    records = []
    with open(filename) as file:
        lines = file.readlines()
        return csv_as_instances(lines, cls, headers)


def csv_as_dicts(lines: list[str], types: list,
                 headers: Optional[str] = None) -> list[dict]:
    records = []
    headers = headers or lines[0]
    lines = lines[1:] if headers else lines
    for line in lines:
        record = {name: func(val) for name, func, val
                  in zip(headers.split(','), types, line.split(','))}
        records.append(record)
    return records


def csv_as_instances(lines: list[str], cls: object,
                     headers: bool = False) -> list[object]:
    records = []
    headers = headers or lines[0]
    lines = lines[1:] if headers else lines
    for line in lines:
        record = cls.from_row(line.split(','))
        records.append(record)
    return records


if __name__ == '__main__':
    path1 = Path('../../Data/portfolio.csv')
    path2 = Path('../../Data/portfolio_noheader.csv')

    port = read_csv_as_dicts(path1, [str, int, float])
    print(port)
    port = read_csv_as_dicts(path2, [str, int, float], headers='name,shares,price')
    print(port)
    port = read_csv_as_instances(path1, Stock, headers=True)
    print(port)
