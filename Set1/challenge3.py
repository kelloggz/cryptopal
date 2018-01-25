import binascii
from operator import itemgetter

from challenge2 import XORop
from charFrqcy import score

scores = {}


def createKey(encStr, keyBytes):
    key = ''
    for i in range(len(encStr)):
        key += keyBytes[i%len(keyBytes)]
    return (key.encode())


    if __name__ == '__main__':
        encryptedString = input()
        try:
            encryptedString = binascii.unhexlify(encryptedString)
            print(encryptedString)
            print(len(encryptedString))
        except:
            print('invalid input')

        for i in range(256):
            keyChar = 'ICE'
            key = createKey(encryptedString, keyChar)
            decryptedString = XORop(encryptedString, key)
        scores[decryptedString] = score(decryptedString)
    print(max(scores.items(), key=itemgetter(1)))
