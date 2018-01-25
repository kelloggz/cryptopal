#############################
#                           #
#   Convert hex to base64   #
#                           #
#                           #
#############################
import base64
import binascii
import codecs

def toBase(str):
    basestr=binascii.unhexlify(str)
    basestr=base64.b64encode(basestr)
    return basestr

def toHex(str):
    string=str.encode()
    hexstr=binascii.hexlify(string)
    return hexstr
