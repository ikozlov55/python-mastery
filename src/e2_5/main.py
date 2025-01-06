import collections
import csv
import tracemalloc
from pathlib import Path


def read_rides_as_columns(filename):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)


def read_rides_as_dicts(filename):
    '''
    Read the bus ride data as a list of dicts
    '''
    records = RideData()  # <--- CHANGE THIS
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides
            }
            records.append(record)
    return records


class RideData(collections.abc.Sequence):
    def __init__(self):
        self.routes = []  # Columns
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        return len(self.routes)

    def __getitem__(self, index):
        if isinstance(index, slice):
            start, stop, step = index.start, index.stop, index.step
            item = RideData()
            item.routes = self.routes[start:stop:step]
            item.dates = self.dates[start:stop:step]
            item.daytypes = self.daytypes[start:stop:step]
            item.numrides = self.numrides[start:stop:step]
            return item
        else:
            return {
                'route': self.routes[index],
                'date': self.dates[index],
                'daytype': self.daytypes[index],
                'rides': self.numrides[index]
            }

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])


path = Path(__file__).parent / '../..' / 'Data/ctabus.csv'
tracemalloc.start()
records = read_rides_as_dicts(path)
tracemalloc.get_traced_memory()
print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
print(records[0])
r = records[0:10]
print(r)
print(len(r))
print(r[0])
print(r[1])
