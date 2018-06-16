'''
1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
'''

charFrequency = {"\t":1, " ":67, ",":4, ".":4, "a":29,
 				 "c":16, "b":3, "e":37, "d":18, "g":3,
 				 "f":3,  "i":42, "h":1, "m":17, "l":21,
 				 "o":29, "n":24, "q":5, "p":11, "s":18,
 				 "r":22, "u":28, "t":32,"v":3,  "x":3}

hexStr = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

def score(messageStr):
	total = 0
	for char in messageStr:
		if char in charFrequency:
			total += charFrequency[char]
	return total

# idk why .join() isn't working rip
def decodeMessage(hexStr):
	score_message_map = {}
	for k in range(256):
		message = ''
		for i in range(0, len(hexStr), 2):
			message += chr(int(hexStr[i:i+2], 16) ^ k)
		score_message_map[score(message)] = message
	message = score_message_map[max(score_message_map)]
	assert(message == "Cooking MC's like a pound of bacon")
	return message

print(decodeMessage(hexStr))