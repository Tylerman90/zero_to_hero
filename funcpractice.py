def lesser_of_two_evens(a,b):
	if a%2 == 0 and b%2 == 0:
		if a > b:
			return(b)
		else:
			return(a)
	elif a%3 == 0 or b%3 == 0:
		if a > b:
			return(a)
		else:
			return(b)
	else:
		print("Come on! Why do you have to make everything so complicated!")


def animal_crackers(words):
	two_words = words.split()
	if two_words[0][0].lower() == two_words[1][0].lower():
		return True
	else:
		return False

print(animal_crackers('Crazy Kangaroo'))

