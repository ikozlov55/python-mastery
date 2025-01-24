import os
import time


def follow(path):
    f = open(path)
    f.seek(0, os.SEEK_END)
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)  # Sleep briefly and retry
            continue
        yield line
