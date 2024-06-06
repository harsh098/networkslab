import socket

try:
    s = socket.socket()

    s.connect(('127.0.0.1', 12345))

    print(s.recv(1024).decode())
except socket.gaierror:
    exit(1)
finally:
    s.shutdown(socket.SHUT_RD)
    s.close()