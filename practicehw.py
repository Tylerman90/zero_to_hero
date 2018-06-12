def multiply(numbers):
	total = 1
	for i in numbers:
		total = total * i
	return total

print(multiply([1,2,3,-4]))


def palindrome(s):
	for letters in s:
		if s[0::] == s[::-1]:
			return True
		else:
			return False

#print(palindrome('helleh'))


import string

def ispangram(strl, alphabet=string.ascii_lowercase):
	for letter in alphabet:
		if letter not in strl:
			return False
		else:
			return True

print(ispangram("The quick brown fox jumps over the lazy dog"))
















