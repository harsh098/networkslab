import socket
import json
class RPCServer:
    def __init__(self, port=12345, address='0.0.0.0'):
        self.__port = port
        self.__address = address
        self.__methods = dict()
    
    def register_function(self, func):
        self.__methods[func.__name__] = func
    
    def __fallback(self, *args, **kwargs):
        return "Function not registered"

    def call(self, func, *args, **kwargs):
        func = self.__methods.get(func, None)
        if not func:
            return self.__fallback()

        return func(*args, **kwargs)

    def run(self):
        with socket.socket() as sock:
            sock.bind((self.__address, self.__port))
            sock.listen(10)
            while True:
                try:
                    client, address = sock.accept()
                    print("Connected to ", address)
                    query = client.recv(1024).decode('utf-8')
                    query = json.loads(query)        
                    answer = str(self.call(query['func'], *(query['f_args']), *(query['f_kwargs'])))
                    response = json.dumps({ 
                        'response': answer,
                    }).encode()
                    client.send(response)
                except OSError:
                    client.close()
                except EOFError:
                    client.close()
                except KeyError:
                    client.send("Error in query".encode())
                    client.close()
                except KeyboardInterrupt:
                    break
                finally:
                    if client:
                        client.close()
