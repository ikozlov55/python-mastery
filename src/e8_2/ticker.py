import csv
from pathlib import Path

from follow import follow
from src.e3_8.tableformat import print_table, create_formatter
from structure import Structure
from validate import String, Float, Integer


class Ticker(Structure):
    name = String()
    price = Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()


if __name__ == '__main__':
    path = Path(__file__).parent / '../..' / 'Data/stocklog.csv'
    formatter = create_formatter('text')

    lines = follow(path)
    rows = csv.reader(lines)
    records = (Ticker.from_row(row) for row in rows)
    negative = (rec for rec in records if rec.change < 0)
    print_table(negative, ['name', 'price', 'change'], formatter)
