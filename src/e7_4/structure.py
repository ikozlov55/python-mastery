from validate import validate_attributes, String, PositiveFloat, PositiveInteger


class Structure:
    _types = ()

    @classmethod
    def create_init(cls):
        args_str = ', '.join(cls._fields)
        code = f'def __init__(self, {args_str}):'
        for arg in cls._fields:
            code += f'\n\tself.{arg} = {arg}'
        locs = {}
        exec(code, locs)
        cls.__init__ = locs['__init__']

    @classmethod
    def from_row(cls, row):
        rowdata = [func(val) for func, val in zip(cls._types, row)]
        return cls(*rowdata)

    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)

    def __repr__(self):
        fields = ', '.join(str(getattr(self, f)) for f in self._fields)
        return f'{self.__class__.__name__}({fields})'

    def __setattr__(self, key, value):
        if not key in self._fields and not key.startswith('_'):
            raise AttributeError(f'No attribute {key}')
        super().__setattr__(key, value)


def typed_structure(clsname, **validators):
    cls = type(clsname, (Structure,), validators)
    return cls


if __name__ == '__main__':
    Stock = typed_structure('Stock', name=String(), shares=PositiveInteger(), price=PositiveFloat())
    s = Stock('GOOG', 100, 490.1)
    print(s.name)
    print(s)
