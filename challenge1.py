#############################
#                           #
#   Convert hex to base64   #
#                           #
#                           #
#############################
import base64
import binascii


def toBase(str):
    basestr=binascii.unhexlify(str)
    basestr=base64.b64encode(basestr)
    return basestr

string=input()

expected=b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

if toBase(string)==expected:
    print("Program works")
else:
    print("Program does not work")
