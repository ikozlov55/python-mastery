import csv
from pathlib import Path

path = Path(__file__).parent / '../..' / 'Data/portfolio.csv'
coltypes = [str, int, float]
f = open(path)
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
record = {name: func(val) for name, func, val in zip(headers, coltypes, row)}
print(record)
