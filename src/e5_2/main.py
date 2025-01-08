import threading
import time
from concurrent.futures import Future, ThreadPoolExecutor


def parse_line(line: str):
    parts = line.split('=')
    return tuple(parts) if len(parts) == 2 else None


print(parse_line('email=guido@python.org'))
print(parse_line('spam'))


def worker(x, y):
    print('About to work')
    time.sleep(3)
    print('Done')
    return x + y


def do_work(x, y, fut):
    fut.set_result(worker(x, y))


fut = Future()
t = threading.Thread(target=do_work, args=(2, 3, fut))
t.start()
result = fut.result()
print(result)

pool = ThreadPoolExecutor()
fut = pool.submit(worker, 2, 3)
print(fut.result())
