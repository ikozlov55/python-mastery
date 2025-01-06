import csv
import tracemalloc
from pathlib import Path
from typing import NamedTuple


class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


class RowTuple(NamedTuple):
    route: str
    date: str
    daytype: str
    rides: int


class RowWithSlots:
    __slots__ = ['route', 'date', 'daytype', 'rides']

    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def read_rides_as_strings(filename):
    with open(path, 'r') as file:
        records = file.readlines()
    return records


def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_dicts(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            record = {
                'route': row[0],
                'date': row[1],
                'daytype': row[2],
                'rides': int(row[3]),
            }
            records.append(record)
    return records


def read_rides_as_row_objects(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            record = Row(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records


def read_rides_as_named_tuples(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            record = RowTuple(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records


def read_rides_as_row_objects_with_slots(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            record = RowWithSlots(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records


if __name__ == '__main__':
    tracemalloc.start()
    path = Path(__file__).parent / '../..' / 'Data/ctabus.csv'
    # rows = read_rides_as_strings(path) # Memory Use: Current 45351007, Peak 45368802
    # rows = read_rides_as_tuples(path) # Memory Use: Current 123688567, Peak 123723226
    # rows = read_rides_as_dicts(path) # Memory Use: Current 188372567, Peak 188407226
    # rows = read_rides_as_row_objects(path) # Memory Use: Current 142174191, Peak 142208850
    # rows = read_rides_as_named_tuples(path)  # Memory Use: Current 128310583, Peak 128344474
    # rows = read_rides_as_row_objects_with_slots(path) # Memory Use: Current 119068911, Peak 119103570
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
