from collections import deque
from socket import *
from types import coroutine

from select import select

tasks = deque()
recv_wait = {}  # sock -> task
send_wait = {}  # sock -> task


def run():
    while any([tasks, recv_wait, send_wait]):
        while not tasks:
            can_recv, can_send, _ = select(recv_wait, send_wait, [])
            for s in can_recv:
                tasks.append(recv_wait.pop(s))
            for s in can_send:
                tasks.append(send_wait.pop(s))
        task = tasks.popleft()
        try:
            reason, resource = task.send(None)
            if reason == 'recv':
                recv_wait[resource] = task
            elif reason == 'send':
                send_wait[resource] = task
            else:
                raise RuntimeError('Unknown reason %r' % reason)
        except StopIteration:
            print('Task done')


class GenSocket:
    def __init__(self, socket):
        self.socket = socket

    @coroutine
    def accept(self):
        yield 'recv', self.socket
        client, addr = self.socket.accept()
        return GenSocket(client), addr

    @coroutine
    def recv(self, maxsize):
        yield 'recv', self.socket
        return self.socket.recv(maxsize)

    @coroutine
    def send(self, data):
        yield 'send', self.socket
        return self.socket.send(data)

    def __getattr__(self, name):
        return getattr(self.socket, name)


async def tcp_server(address, handler):
    sock = GenSocket(socket(AF_INET, SOCK_STREAM))
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = await sock.accept()
        tasks.append(handler(client, addr))


async def echo_handler(client, address):
    print('Connection from', address)
    while True:
        data = await client.recv(1000)
        if not data:
            break
        await client.send(b'GOT:' + data)
    print('Connection closed')


if __name__ == '__main__':
    tasks.append(tcp_server(('', 25000), echo_handler))
    run()
