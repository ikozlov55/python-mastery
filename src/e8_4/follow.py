import os
import time
from pathlib import Path


def follow(filename):
    try:
        with open(filename, 'r') as f:
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline()
                if line == '':
                    time.sleep(0.1)  # Sleep briefly to avoid busy wait
                    continue
                yield line
    except GeneratorExit:
        print('Following Done')


if __name__ == '__main__':
    path = Path(__file__).parent / '../..' / 'Data/stocklog.csv'
    f = follow(path)
    for line in f:
        print(line, end='')
        if 'IBM' in line:
            break

    for line in f:
        print(line, end='')
        if 'IBM' in line:
            break
