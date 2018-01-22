
#Write a function that takes two equal-length buffers and produces their XOR combination.

import binascii


def XORop(buffer1, buffer2):
    if len(buffer1) != len(buffer2):
        return print('Buffer not same length')
    else:
        XORbuffer = ''.join(chr(i ^ j) for i, j in zip(buffer1, buffer2))
        return XORbuffer


buffer1 = input('String1:')
buffer2 = input('String2:')

buffer1 = binascii.unhexlify(buffer1)
print(buffer1)
buffer2 = binascii.unhexlify(buffer2)
print(buffer2)

result = XORop(buffer1, buffer2)
print(binascii.hexlify(result.encode()))
