import sys
import re



def check_punctuation(char):
	if char >= "!" and char <= "/":
		return True
	return False
# parci hadechi 
def text_analyzer(str):
	
	count_space = str.count(" ")
	count_upper = 0
	count_lower = 0
	count_punctuation = 0
	count_upper = sum(1 for char in str if char.isupper())
	count_lower = sum(1 for char in str if char.islower())
	count_punctuation = sum(1 for char in str if check_punctuation(char))
	
	print(f"The text contains 143 printable character(s):\n- {count_upper} upper letter(s)\n- {count_lower} lower letter(s)\n- {count_punctuation} punctuation mark(s)\n- {count_space} space(s)\n")

if (__name__ == "__main__"):
	text_analyzer("Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles.")
