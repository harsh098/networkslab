def calculateCheckSum(frames, frame_size):
    checksum = frames[0]
    for i in range(1, len(frames)):
        checksum = str(bin(int(checksum, 2)+ int(frames[i], 2)))[2:]
        while len(checksum) > frame_size:
            frame_bits = checksum[len(checksum)-frame_size:]
            carry_bits = checksum[:len(checksum)-frame_size]
            checksum = str(bin(int(frame_bits, 2) + int(carry_bits, 2)))[2:]
        if len(checksum) < frame_size:
            checksum = ("0"*(frame_size - len(checksum))) + checksum
    final_checksum = ''
    for bit in checksum:
        final_checksum+= '0' if bit=='1' else '1'

    return final_checksum


def send_data(frame_size, message):
    k = frame_size
    prev = 0
    frames = []
    for j in range(len(message)//k):
        frames.append(message[prev: prev+k])
        prev = k*(j+1)
    print("Received Message: ", message)
    print("Frame_Size:", frame_size)
    print("Frames: ", frames)
    checksum = calculateCheckSum(frames, frame_size)
    return [checksum] + frames



def verify_checksum(frame_size, frames):
    checksum =  frames[0]
    for i in range(1, len(frames)):
        checksum = str(bin(int(checksum, 2) + int(frames[i], 2)))[2:]
    while len(checksum) > frame_size:
        frame_bits = checksum[len(checksum)-frame_size :]
        carry_bits = checksum[:len(checksum)-frame_size]
        checksum = str(bin(int(frame_bits, 2) + int(carry_bits, 2)))[2:]

    if checksum == '1'*frame_size:
        print("Verified Result:\nChecksum= ",checksum)
    else:
        print("Invalid checksum: ", checksum)

sent_data = send_data(5, '10101011111101110001')
print("Sending Data: ", sent_data)
verify_checksum(5, sent_data)
