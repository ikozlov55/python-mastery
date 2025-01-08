def typedproperty(expected_type):
    class Descriptor:
        @property
        def value(self):
            return getattr(self, self.private_name)

        @value.setter
        def value(self, val):
            if not isinstance(val, expected_type):
                raise TypeError(f'Expected {expected_type}')
            setattr(self, self.private_name, val)

        def __set_name__(self, instance, name):
            self.private_name = '_' + name

    return Descriptor()


def String():
    return typedproperty(str)


def Integer():
    return typedproperty(int)


def Float():
    return typedproperty(float)


class Stock:
    name = String()
    shares = Integer()
    price = Float()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __str__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'

if __name__ == '__main__':
    goog = Stock('GOOG', 100, 490.10)
    goog.price = 450.5
    print(goog.name)
    print(goog.shares)
    print(goog.price)
