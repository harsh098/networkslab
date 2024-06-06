from rpc import RPCClient

client = RPCClient()
print(client.call('add', 1, 2))