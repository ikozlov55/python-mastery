class Validator:

    def __set_name__(self, cls, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)


class Typed(Validator):
    expected_type = object

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return super().check(value)


class Integer(Typed):
    expected_type = int


class Float(Typed):
    expected_type = float


class String(Typed):
    expected_type = str


class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        return super().check(value)


class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError('Must be non-empty')
        return super().check(value)


class PositiveInteger(Integer, Positive):
    pass


class PositiveFloat(Float, Positive):
    pass


class NonEmptyString(String, NonEmpty):
    pass


class Stock:
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares = self.shares - nshares if nshares < self.shares else 0

    @classmethod
    def from_row(cls, row):
        return cls(*[func(val) for func, val in zip(cls._types, row)])

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.shares}, {self.price})'

    def __eq__(self, other):
        return isinstance(other, self.__class__) and ((self.name, self.shares, self.price) ==
                                                      (other.name, other.shares, other.price))


s = Stock('GOOG', 100, 490.10)
s.price = 10.0
print(s)
