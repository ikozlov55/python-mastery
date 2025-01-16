import sys


class Structure:

    @staticmethod
    def _init():
        locs = sys._getframe(1).f_locals
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)

    def __repr__(self):
        fields = ', '.join(str(getattr(self, f)) for f in self._fields)
        return f'{self.__class__.__name__}({fields})'

    def __setattr__(self, key, value):
        if not key in self._fields and not key.startswith('_'):
            raise AttributeError(f'No attribute {key}')
        super().__setattr__(key, value)


class Stock(Structure):
    _fields = ('name', 'shares', 'price')


class Date(Structure):
    _fields = ('year', 'month', 'day')


if __name__ == '__main__':
    s = Stock('GOOG', 100, 490.1)
    print(s.name)
    print(s.shares)
    print(s.price)
    print(repr(s))
    s._shares = 400.5
    print(s.__dict__)
