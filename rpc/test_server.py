from rpc import RPCServer


def add(a,b):
    return int(a)+int(b)

server = RPCServer()
server.register_function(add)
server.run()