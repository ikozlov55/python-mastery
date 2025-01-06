import csv
import tracemalloc
from pathlib import Path

from src.e2_1.readrides import read_rides_as_dicts
path = Path(__file__).parent / '../..' / 'Data/ctabus.csv'

# tracemalloc.start()
# rows = read_rides_as_dicts(path)
# rt22 = [row for row in rows if row['route'] == '22']
#
# print(max(rt22, key=lambda row: row['rides']))
# print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())

tracemalloc.start()
f = open(path)
f_csv = csv.reader(f)
headers = next(f_csv)
rows = (dict(zip(headers, row)) for row in f_csv)
rt22 = (row for row in rows if row['route'] == '22')
print(max(rt22, key=lambda row: row['rides']))
print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
