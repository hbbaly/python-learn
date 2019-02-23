import socket
import threading
import time


def tcplink(sock, addr):
    print('Accept new connection from {0[0]}:{0[1]}'.format(addr))
    sock.send(b'welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, {}!'.format(data.decode('utf-8')).encode('utf-8')))
    sock.close()
    print('Connection from {0[0]}:{0[1]} closed'.format(addr))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('Waiting for connection...')
while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()