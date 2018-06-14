"""
Convert hex to base64
---------------------
The string:
49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573\
206d757368726f6f6d

Should produce:
SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

So go ahead and make that happen. You'll need to use this code for the rest of
the exercises.

"""

# Hand Conversion
# 4 9 2 7
# 00000100 00001001 00000010 00000111 0000

# 000001 000000 100100 000010 000001 110000
# 1      0      36     2      1      48


# 4     9     2     7
# 0100  1001  0010  0111


# 010010 010010
# S        S

import binascii

def convertHexToBase64(hexStr):
	# convert hexstring to binary, then convert binary to base64
	return binascii.b2a_base64(binascii.unhexlify(hexStr))

print(convertHexToBase64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573\
206d757368726f6f6d"))
