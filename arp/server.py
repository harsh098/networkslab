import socket


arp_table = {
    '192.168.0.2' : '12:22:2a:3b:4a:6c',
    '12:22:2a:3b:4a:6c': '192.168.0.2',
}

try:
    s = socket.socket()
    print("Socket Created")
    s.bind(('0.0.0.0', 12345))
    s.listen(5)
    print("Listening at .....")
    while True:
        client, address = s.accept()
        print("Got Connection from...", address)
        query = client.recv(1024).decode("utf-8")
        result = arp_table.get(query, "Not Found in ARP Table")
        client.send(result.encode())
except KeyboardInterrupt:
    print("Exiting....")
finally:
    s.shutdown(socket.SHUT_RDWR)
    s.close()