from logcall import logged, logformat


@logformat('{func.__code__.co_filename}:{func.__name__}')
def add(x, y):
    'Adds two things'
    return x + y


@logformat('Calling {func.__name__}')
def sub(x, y):
    return x - y


class Spam:
    @logged
    def instance_method(self):
        pass

    @logged
    @classmethod
    def class_method(cls):
        pass

    @logged
    @staticmethod
    def static_method():
        pass

    @logged
    @property
    def property_method(self):
        pass


if __name__ == '__main__':
    print(help(add))
    print(add.__name__)
    print(add.__doc__)
    print(add(2, 3))
    print(sub(5, 1))

    s = Spam()
    s.instance_method()
    #Spam.class_method()
    Spam.static_method()
    print(s.property_method)
