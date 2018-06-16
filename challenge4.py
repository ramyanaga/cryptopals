from challenge3 import decodeMessage, score

def findEncryptedLine(fileName):
	lines = [line.rstrip('\n') for line in open(fileName)]
	score_decryptedLine_map = {}

	for line in lines:
		decodedLine = decodeMessage(line)
		score_decryptedLine_map[score(decodedLine)] = decodedLine
	
	return score_decryptedLine_map[max(score_decryptedLine_map)]

print(findEncryptedLine("challenge4.txt"))



