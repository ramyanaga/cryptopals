englishStr = "Burning \'em, if you ain\'t quick and nimble\n I go crazy when I hear a cymbal"
key = "ICE"


# idk if this is right???
def repeatingKeyXOR(string, key):
	encryptedMessage = ""
	i = 0
	while i < len(englishStr):
		encryptedMessage += hex(int(ord(englishStr[i])) ^ int(ord(key[i%len(key)])))
		i+=1
	return encryptedMessage

def repeatingKeyXOR(string, key):
	key = key*(len(englishStr)//len(key)) + key[0:len(englishStr)%len(key)]
	encryptedStr = ''
	for i in range(0, len(string)):
		encryptedStr += hex(ord(string[i]) ^ ord(key[i]))
	return encryptedStr

print(repeatingKeyXOR(englishStr, key))
result = repeatingKeyXOR(englishStr, key)
print(type(result))
correctEncryption = ("0b3637272a2b2e63622"+ 
					 "c2e69692a23693a2a3c63" + 
					 "24202d623d63343" + 
					 "c2a26226324272765272"
					 "a282b2f20430a652e2c" + 
					 "652a3124333a653e2" + 
					 "b2027630c692b202831" + 
					 "65286326302e27282f")
#assert(bin(int(correctEncryption, 16)) == bin(int(str(result)), 16))

