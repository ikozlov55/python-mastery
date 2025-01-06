from collections import Counter
from pathlib import Path

from src.e2_1.readrides import read_rides_as_dicts

path = Path(__file__).parent / '../..' / 'Data/ctabus.csv'
records = read_rides_as_dicts(path)
routes = {x['route'] for x in records}

print('How many bus routes exist in Chicago?')
print(len(routes))
print()

print('How many people rode the number 22 bus on February 2, 2011? What about any route on any date of your choosing?')
rides_per_date = {(x['route'], x['date']): x['rides'] for x in records}
print(rides_per_date['22', '02/02/2011'])
print()

print('What is the total number of rides taken on each bus route?')
rides_per_route = Counter()
for x in records:
    rides_per_route[x['route']] += x['rides']
print(rides_per_route)
print()

print('What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?')
rides_per_year = Counter()
for x in records:
    year = x['date'].split('/')[-1]
    if year not in {'2001', '2011'}:
        continue
    rides_per_year[(x['route'], year)] += x['rides']

ridership_increase = Counter()
for route in {x['route'] for x in records}:
    ridership_increase[route] += rides_per_year[(route, '2011')]
    ridership_increase[route] -= rides_per_year[(route, '2001')]
print(ridership_increase.most_common(5))
