import os
import time
from functools import wraps


# Data source
def follow(filename, target):
    with open(filename, 'r') as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if line != '':
                target.send(line)
            else:
                time.sleep(0.1)


# Decorator for coroutine functions
def consumer(func):
    @wraps(func)
    def start(*args, **kwargs):
        f = func(*args, **kwargs)
        f.send(None)
        return f

    return start


@consumer
def printer():
    while True:
        try:
            item = yield
            print(item)
        except Exception as e:
            print('ERROR: %r' % e)


def receive(expected_type):
    msg = yield
    assert isinstance(msg, expected_type), 'Expected type %s' % (expected_type)
    return msg


@consumer
def print_ints():
    while True:
        val = yield from receive(int)
        print('Got:', val)


if __name__ == '__main__':
    p = print_ints()
    p.send(1)
    p.send(22)
    p.send('zz')
