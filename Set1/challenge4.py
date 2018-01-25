import binascii

from challenge2 import XORop
from challenge3 import createKey
from charFrqcy import score
from operator import itemgetter
list1 = {}


with open('challenge4text.txt', 'r') as ciphertexts:
    for line in ciphertexts:
        encryptedString = line.strip()
        print('Line '+encryptedString+' will now be tested:')
        encryptedString = binascii.unhexlify(encryptedString)
        for i in range(256):
            keyChar = chr(i)
            key = createKey(encryptedString, keyChar)
            decryptedString = XORop(encryptedString, key)
            list1['KeyChar: '+keyChar+' Zeile: '+line+' Plaintext: '+decryptedString]=score(decryptedString)
print(max(list1.items(), key=itemgetter(1)))
