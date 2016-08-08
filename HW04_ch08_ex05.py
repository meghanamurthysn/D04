# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 5 for the task.
# Please do provide function calls that test/demonstrate your
# function.
################################################################################
def rot_letter(letter, n):
	""" Rotate a letter by n places"""
	if letter.islower():
		return chr((ord(letter) - ord('a')+n) % 26 + ord('a'))
	elif letter.isupper():
		return chr((ord(letter) - ord('A')+n) % 26 + ord('A'))
	else:
		return letter

def rot_word(word, n):
	""" Rotate each letter in a word by n places"""
	result_word = ''
	for letter in word:
		result_word += rot_letter(letter, n)
	return result_word

################################################################################
def main():
    print(rot_word('cheer', 7))
    print(rot_word('melon', -10))
    print(rot_word('IBM', -1))

if __name__ == '__main__':
    main()