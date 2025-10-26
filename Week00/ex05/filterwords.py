import sys
import string

av = sys.argv
ac = av.__len__()

def check_punctuation(char):
	if char >= "!" and char <= "/":
		return True
	return False

try:
	if (ac != 3):
		raise ValueError("invalid args number")
	punctuation_chars = string.punctuation
	N = int(av[2])
	S = av[1]
	# print(N)
	# print(S)
	split = S.split(" ")

	print(split)
	list = [string for string in split if string.count() >= N]
except ValueError as e:
	print(f"{e}")
