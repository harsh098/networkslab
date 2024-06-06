import socket

try:
    s = socket.socket()
    s.connect(('127.0.0.1', 12345))
    mode = ''
    while mode.strip().upper() not in ["RARP", "ARP"]:
        print("Enter 'ARP' for ARP Request and 'RARP' for RARP request")
        mode = input("RARP or ARP: ").upper().strip()
    query = input(f"Enter {'ip' if mode=='ARP' else 'mac' }: ")
    print("Sending ", mode, " request...")
    s.send(query.encode())
    print("Response from ARP Server:  ", s.recv(1024).decode('utf-8')) 
except socket.gaierror:
    print("ARP Server Not Available")
finally:
    s.shutdown(socket.SHUT_RDWR)
    s.close()