class SimpleStock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price


goog = SimpleStock('GOOG', 100, 490.10)
goog.date = '6/11/2007'
goog.__dict__['time'] = '9:45am'
print(goog.__dict__)
print(goog.__class__)
print()

ibm = SimpleStock('IBM', 50, 91.23)
print(ibm.__dict__)
print(ibm.__class__)
print()

print(SimpleStock.__dict__['cost'])
print(SimpleStock.__dict__['cost'](goog))
SimpleStock.spam = 42
print(goog.spam)
print(ibm.spam)
