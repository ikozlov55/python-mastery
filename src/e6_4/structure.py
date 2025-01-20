class Structure:

    @classmethod
    def create_init(cls):
        args_str = ', '.join(cls._fields)
        code = f'def __init__(self, {args_str}):'
        for arg in cls._fields:
            code += f'\n\tself.{arg} = {arg}'
        locs = {}
        exec(code, locs)
        cls.__init__ = locs['__init__']

    def __repr__(self):
        fields = ', '.join(str(getattr(self, f)) for f in self._fields)
        return f'{self.__class__.__name__}({fields})'

    def __setattr__(self, key, value):
        if not key in self._fields and not key.startswith('_'):
            raise AttributeError(f'No attribute {key}')
        super().__setattr__(key, value)
