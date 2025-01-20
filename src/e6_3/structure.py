import inspect
import sys


class Structure:

    @staticmethod
    def _init():
        locs = sys._getframe(1).f_locals
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)

    @classmethod
    def set_fields(cls):
        sig = inspect.signature(cls)
        cls._fields = sig.parameters

    def __repr__(self):
        fields = ', '.join(str(getattr(self, f)) for f in self._fields)
        return f'{self.__class__.__name__}({fields})'

    def __setattr__(self, key, value):
        if not key in self._fields and not key.startswith('_'):
            raise AttributeError(f'No attribute {key}')
        super().__setattr__(key, value)
