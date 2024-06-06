import socket, json
class RPCClient:
    def __init__(self, port=12345, address='127.0.0.1'):
        self.__port = port
        self.__address = address
    
    def call(self, func, *args, **kwargs):
        with socket.socket() as sock:
            sock.connect((self.__address, self.__port))
            query = json.dumps({
                'func': func,
                'f_args': args,
                'f_kwargs': kwargs
            }).encode()
            sock.send(query)
            response = sock.recv(1024).decode('utf-8')
            response = json.loads(response)
            answer = response['response']
        
        return answer

