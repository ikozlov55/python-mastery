from functools import wraps


def logged(func):
    name = func.fget.__name__ if isinstance(func, property) else func.__name__
    print('Adding logging to', name)

    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Calling', name)
        return func(*args, **kwargs)

    return wrapper


def logformat(fmt):
    def outer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)

        return wrapper

    return outer
