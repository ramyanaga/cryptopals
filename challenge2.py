"""
Fixed XOR
---------
Write a function that takes two equal-length buffers and produces their XOR
combination.

If your function works properly, then when you feed it the string:
1c0111001f010100061a024b53535009181c

... after hex decoding, and when XOR'd against:
686974207468652062756c6c277320657965

... should produce:
746865206b696420646f6e277420706c6179
"""


# 0001 1100 0000

# 0110 1000 0110

# 0111 0100 0110
# 7    4    6

# Steps:
# 1. convert to binary
# 2. XOR

import binascii

def fixedXOR(hexStr):
	fixedXORStr = "686974207468652062756c6c277320657965"
	XORStr = hex(int(hexStr, 16) ^ int(fixedXORStr, 16))
	return XORStr

print(fixedXOR("1c0111001f010100061a024b53535009181c"))
