# Write a function that takes two equal-length buffers and produces their XOR combination.
import binascii


def XORop(buffer1, buffer2):
    try:
        XORbuffer = ''.join(chr(i ^ j) for i, j in zip(buffer1, buffer2))
        return XORbuffer
    except:
        print('invalid input')


if __name__ == '__main__':
    string1 = '1c0111001f010100061a024b53535009181c'

    decodedString = binascii.unhexlify(string1)
    print("String1: ",decodedString)

    string2 = '686974207468652062756c6c277320657965'
    decodedString2=binascii.unhexlify(string2)
    print("String2: ", decodedString2)


    expected = '746865206b696420646f6e277420706c6179'
    decrypted=(XORop(decodedString,decodedString2)).encode()

    if(binascii.hexlify(decrypted).decode()==expected):
        print("Challenge Done")
    else:
        print("Try agein")




