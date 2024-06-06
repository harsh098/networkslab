import socket
try:
    s = socket.socket()
    print("Socket creation successfull")

    s.bind(('0.0.0.0', 12345))

    print("Bind socket to port no: 12345")

    s.listen(5)
    while True:
        client, address = s.accept()
        print("Got connection from: ", address)
        client.send("Hello".encode())
        client.close()
except KeyboardInterrupt:
    print("Exiting...")
finally:
    print("Performing Graceful Shutdown")
    s.shutdown(socket.SHUT_WR)
    s.close()






