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


class ValidatedFunction:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        sig = inspect.signature(self.func)
        bound = sig.bind(*args, **kwargs)
        for name, value in bound.arguments.items():
            validator = self.func.__annotations__[name]
            if hasattr(validator, 'check'):
                validator.check(value)
        result = self.func(*args, **kwargs)
        return result


def add(x: int, y: PositiveInteger):
    return x + y


if __name__ == '__main__':
    add = ValidatedFunction(add)
    print(add(2, 3))
    print(add(2, -1))
