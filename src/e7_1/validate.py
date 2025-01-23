import inspect


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


def validated(func):
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound = sig.bind(*args, **kwargs)
        errors = []
        for name, value in bound.arguments.items():
            if name == 'self':
                continue
            validator = func.__annotations__[name]
            if hasattr(validator, 'check'):
                try:
                    validator.check(value)
                except (TypeError, ValueError) as e:
                    errors.append(f'\t{e}')
        if errors:
            raise TypeError('Bad Arguments\n' + '\n'.join(errors))
        result = func(*args, **kwargs)
        return result

    return wrapper


@validated
def add(x: Integer, y: Integer):
    return x + y


class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @validated
    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares


if __name__ == '__main__':
    print(add(2, 3))
    print(add('2', '3'))

    stock = Stock('GOOG', 50, 100)
    stock.sell(10)
    print(stock.shares)
    stock.sell(-10)
