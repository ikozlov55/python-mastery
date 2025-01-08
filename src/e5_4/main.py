def counter(value):
    def incr():
        nonlocal value
        value += 1
        print(value)
        return value

    def decr():
        nonlocal value
        value -= 1
        print(value)
        return value

    return incr, decr


up, down = counter(0)
up()
up()
up()
up()
down()
down()
down()