def xor(a,b):
    result = ''
    for i in range(1, len(a)):
        if a[i]==b[i]:
            result+='0'
        else:
            result+='1'
    return result

def mod2div(dividend,divisor):
    pick = len(key)
    tmp = dividend[:pick]
    while pick<len(dividend):
        if tmp[0] == '1':
            tmp = xor(tmp, divisor)+dividend[pick]
        else:
            tmp = xor(tmp, '0'*pick,) + dividend[pick]
        pick+=1
    if tmp[0]=='1':
        tmp = xor(tmp, divisor)
    else:
        tmp = xor(tmp, '0'*pick)
    
    return tmp
    


def encode_data(message, key):
    append_data = message + '0'*(len(key)-1)
    encoded_data = message+mod2div(append_data, key)
    return encoded_data

def check_crc(message, key):
    r = mod2div(message, key)
    if int(r) == 0:
        print("Valid CRC")
    else:
        print("Invalid")


print("Start of Simulation")
print("Sender's end....\n______________")
message = input("Data to send:")
key = input("Agreed CRC Key:")
encoded_data = encode_data(message=message, key=key)
print("Sending: ",encoded_data)
print("Receiver's end....\n______________")
key = input("Agreed CRC Key:")
recv = input("Enter Received Data:")
check_crc(message=recv, key=key)
    