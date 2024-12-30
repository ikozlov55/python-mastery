from src.e1_4 import pcost
from src.e1_5.stock import Stock

print(pcost.portfolio_cost('../../Data/portfolio2.dat'))
s = Stock('GOOG', 100, 490.10)
print(s.name)
print(s.cost())
