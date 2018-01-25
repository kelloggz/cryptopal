from challenge2 import XORop
from challenge3 import createKey
import binascii




if __name__=='__main__':
    plaintext=input()
    plaintext=plaintext
    keystring='ICE'

    print("Das ist der zu verschlüsselnde Text:", plaintext)
    print("Das ist der Key der verwendet wird:", keystring)
    key = createKey(plaintext, keystring)
    print(key)
    print("Der verschlüsselte Text lautet: ", XORop(key, plaintext.encode()))
    print("Der verschlüsselte Text lautet: ", binascii.hexlify(XORop(key, plaintext.encode()).encode()).decode())