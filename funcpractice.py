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


def makes_twenty(n1,n2):
	if n1 + n2 == 20 or n1 == 20 or n2 == 20:
		return True
	else:
		return False
print(makes_twenty(2,3))


def old_macdonald(name):
	new = name.split()
	return (new[0][0].capitalize() + new[0][1:3] + new[0][3].capitalize() + new[0][4:])
print(old_macdonald('macdonald'))


def master_yoda(text):
	yoda = " ".join(reversed(text.split()))
	return yoda

print(master_yoda('I am great'))






























