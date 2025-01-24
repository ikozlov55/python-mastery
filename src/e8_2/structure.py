from collections import ChainMap

from validate import validate_attributes, Validator


class StructureMeta(type):
    @classmethod
    def __prepare__(meta, clsname, bases):
        return ChainMap({}, Validator.validators)

    @staticmethod
    def __new__(meta, name, bases, methods):
        methods = methods.maps[0]
        return super().__new__(meta, name, bases, methods)


class Structure(metaclass=StructureMeta):
    _types = []

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
